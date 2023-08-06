from functools import cached_property
from typing import Any, Mapping, Type, Union

from fastapi.requests import Request
from pydantic.dataclasses import dataclass
from pymongo import ASCENDING, DESCENDING
from pymongo.client_session import ClientSession
from pymongo.collection import Collection
from pymongo.cursor import Cursor

from fastapi_views.pagination.annotations import PaginationKwargs
from fastapi_views.pagination.core import (
    BasePaginationCursor,
    BasePaginationLimitOffset,
    BasePaginatorAPI,
    PaginationBase
)
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record
from fastapi_views.utils import get_regex_group


class PaginationCursor(BasePaginationCursor):
    """Cursor pagination."""

    session: ClientSession
    statement: Mapping[str, Any]
    collection: Collection

    def _filter_query(self, cursor: Cursor) -> Cursor:
        """Extends mongodb query by providing additional where clause."""
        is_next_page = self.decoded_cursor.startswith(self.next_prefix)
        prefix, op = self._get_prefix_and_operator(is_next_page)

        regex_result = get_regex_group(f'(?<={prefix})(.*)(?=&page__)', self.decoded_cursor)
        sign = {
            'lt': '<',
            'gt': '>'
        }
        return cursor.where(f'this.{self.get_first_order_field()} {sign.get(op)} {regex_result}')

    def _create_model_ordering(self) -> None:
        """
        Overridden method to set up correct model_ordering attribute.
        Expected list with key, value tuples to assign : [('field', asc/desc), ...]
        """
        result = []
        ordering = self.kwargs.get('ordering')
        if not ordering:
            self.model_ordering = []
        for f_name in ordering:
            if self.is_ordering_model_field_negative(f_name):
                result.append((get_regex_group('(?<=-).*', f_name), DESCENDING))
            else:
                result.append((f_name, ASCENDING))

        self.model_ordering = result

    def _get_query_result(self) -> list[Record]:
        """Final result that will be returned as object list."""
        results = []
        cursor = self.collection.find(self.statement)

        if self.cursor is not None:
            cursor = self._filter_query(cursor)

        if self.model_ordering:
            cursor = cursor.sort(self.model_ordering).limit(self.limit + 1)
        else:
            cursor = cursor.limit(self.limit + 1)
        for document in cursor:
            results.append(document)
        return results

    def paginate_object_list(
            self,
            request,
            *args,
            **kwargs,
    ) -> list[Record]:
        self.session, self.statement, self.collection = args
        return super().paginate_object_list(request, **kwargs)


class PaginationLimitOffset(BasePaginationLimitOffset):
    """Limit offset pagination."""

    session: Union[ClientSession, None]
    statement: Mapping[str, Any]
    collection: Collection

    def _get_objects(self) -> list[Record]:
        """Final result that will be returned as object list."""
        cursor = self.collection.find(
            self.statement,
        ).limit(self.limit).skip(self.limit * self.page)
        results = []
        for document in cursor:
            results.append(document)
        return results

    @cached_property
    def count(self) -> int:
        """Get number of documents for given statement."""
        return self.collection.count_documents(
            self.statement,
            session=self.session,
        )

    def paginate_object_list(
            self,
            request: Request,
            *args,
            **kwargs: PaginationKwargs,
    ) -> list[Record]:
        self.session, self.statement, self.collection = args
        return super().paginate_object_list(request, **kwargs)


@dataclass(config=BaseConfig)
class PaginatorAPI(BasePaginatorAPI):
    """Paginator API."""

    statement: Mapping[str, Any] = None
    session: Union[ClientSession, None] = None

    def __post_init__(self):
        if self.strategy is None:
            self.strategy = PaginationLimitOffset
        super().__post_init__()

    @property
    def _strategy_data(self) -> list[Any]:
        """Returns only list of current page objects data."""
        self.collection = self.kwargs.pop('collection')
        return self.strategy_instance.paginate_object_list(
            self.request,
            self.session,
            self.statement,
            self.collection,
            **self.kwargs,
        )


def paginate_api(
        statement: Mapping[str, Any],
        request: Request,
        session: Union[ClientSession, None] = None,
        paginate_by: int = 100,
        strategy: Type[PaginationBase] = None,
        kwargs: Union[dict[str, Any], None] = None,
):
    """
    Returns pagination object for given strategy.

    :param statement: mongodb filter query
    :param request: fastapi Request object.
    :param session: session object
    :param paginate_by: number of objects per page
    :param strategy: pagination strategy object
    :param kwargs: optional params passed to strategy'/s paginate_object_list method
    """
    paginator = PaginatorAPI(
        statement=statement,
        request=request,
        session=session,
        strategy=strategy,
        paginate_by=paginate_by,
        kwargs=kwargs,
    )
    return paginator.strategy_response()
