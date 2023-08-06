import abc
import math
from dataclasses import field
from functools import cached_property
from typing import Any, Mapping, Type, Union

from fastapi import HTTPException, status
from fastapi.datastructures import QueryParams
from fastapi.requests import Request
from pydantic.dataclasses import dataclass

from fastapi_views.pagination.annotations import (
    CursorResponse,
    LimitOffsetResponse,
    PaginationKwargs,
    Table
)
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record
from fastapi_views.utils import (
    decode_value,
    dict_to_query_string,
    encode_value,
    get_regex_group
)


class PaginationBase(abc.ABC):

    @abc.abstractmethod
    def paginate_object_list(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def get_paginated_response(self, object_list):
        raise NotImplementedError


class LimitPageException:
    def query_type_exception(self, param: str, expected_type: str) -> Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Invalid query type, <:{param}> should be type of {expected_type}.',
        )

    def query_int_value_exception(self, param: str, condition: str) -> Exception:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=f'Invalid query value, <:{param}> should be {condition}.',
        )


class LimitMixin(LimitPageException):
    paginate_by: int

    def _get_limit(self, query_params: QueryParams) -> int:
        param = 'limit'
        try:
            limit = int(query_params.get('limit', self.paginate_by))
        except ValueError:
            self.query_type_exception(param, 'int')
        else:
            if limit <= 0:
                self.query_int_value_exception(param, 'higher than 0')
            return limit


class PageMixin(LimitPageException):

    def _get_page(self, query_params: QueryParams) -> int:
        param = 'page'
        try:
            page = int(query_params.get(param, 0))
        except ValueError:
            self.query_type_exception(param, 'int')
        else:
            if page < 0:
                self.query_int_value_exception(param, 'higher or equal 0')
            return page


class LimitPageMixin(LimitMixin, PageMixin):
    ...


class BasePaginationCursor(PaginationBase, LimitMixin, abc.ABC):
    """
    Pagination of Ordered Queries.

    Requires model and ordering to be sent via kwargs when calling paginate_api function, like {
            'model': sqlalchemy Model = modelName,
            'ordering': list[str] = ['-id'],
        }
    Negative '-' means descending order when objects are loaded.
    """

    request: Request
    paginate_by: int
    limit: int
    kwargs: Mapping[Any, Any]
    cursor: str
    model_ordering: list[Any]
    object_list: list[Record] = None
    reverse: bool = False
    _objects = None

    def __init__(self):
        self.lt = 'lt'
        self.gt = 'gt'
        self.next_prefix = 'next__'
        self.previous_prefix = 'previous__'

    @abc.abstractmethod
    def _get_query_result(self) -> list[Record]:
        """Execute db query that will return list of records."""

    def _create_model_ordering(self) -> None:
        """
        Override to set behaviour how query will be sorted.

        Ex. self.model_ordering = [('field_one', 1), ('field_two', -1)]
        """
        self.model_ordering = []

    @cached_property
    def model(self) -> Type[Table]:
        return self.kwargs.get('model')

    @property
    def first_order_field(self) -> str:
        return self.kwargs['ordering'][0]

    @cached_property
    def decoded_cursor(self) -> str:
        if self.cursor:
            return decode_value(self.cursor)
        raise ValueError(f'Can not decode {self.cursor}')

    def _setup_next_page_filter_data(self) -> (str, str):
        op = self.lt if self.first_order_field.startswith('-') else self.gt
        return self.next_prefix, op

    def _update_first_ordering_field(self, value: str) -> None:
        self.kwargs['ordering'][0] = value

    def _setup_previous_page_filter_data(self) -> (str, str):
        if self.first_order_field.startswith('-'):  # start point desc
            value = get_regex_group('(?<=-).*', self.first_order_field)
            op = self.gt
        else:  # start point asc
            value = f'-{self.first_order_field}'
            op = self.lt

        self._update_first_ordering_field(value)
        self._create_model_ordering()
        self.reverse = True
        return self.previous_prefix, op

    def _get_prefix_and_operator(self, is_next_page: bool) -> (str, str):
        if is_next_page:
            return self._setup_next_page_filter_data()
        return self._setup_previous_page_filter_data()

    def get_objects(self, result: list[Record]) -> list[Record]:
        if self.reverse:
            return list(reversed(result))
        return result

    def get_first_order_field(self) -> str:
        if self.first_order_field.startswith('-'):
            return get_regex_group('(?<=-).*', self.first_order_field)
        return self.first_order_field

    @property
    def count(self) -> int:
        # count default
        if self.object_list is not None:
            return len(self.object_list)
        return 0

    @cached_property
    def additional_count(self) -> int:
        # count of limit + 1
        return len(self._objects)

    @property
    def has_next(self) -> bool:
        # at least one additional result exists.
        if self.cursor is not None and self.get_current_decoded_page == 0:
            return True
        return self.additional_count > self.limit

    @property
    def has_previous(self) -> bool:
        if self.cursor is None:
            return False
        return self.get_current_decoded_page > 0

    @cached_property
    def get_current_decoded_page(self) -> int:
        return int(get_regex_group('(?<=page__).*', self.decoded_cursor))

    @property
    def _get_next_page(self) -> int:
        if self.cursor is None:
            return 1
        return self.get_current_decoded_page + 1

    @property
    def _get_previous_page(self) -> int:
        if self.cursor is None:
            return 0
        return self.get_current_decoded_page - 1

    def _get_next_url(self) -> Union[str, None]:
        if self.has_next:
            last_object = self.object_list[-1]
            if type(last_object) == dict:
                value = last_object.get(self.get_first_order_field())
            else:
                value = getattr(last_object, self.get_first_order_field())
            return encode_value(
                f'{self.next_prefix}{value}'
                f'&page__{self._get_next_page}')
        return None

    def _get_previous_url(self) -> Union[str, None]:
        if self.has_previous:
            first_object = self.object_list[0]
            if type(first_object) == dict:
                value = first_object.get(self.get_first_order_field())
            else:
                value = getattr(first_object, self.get_first_order_field())
            return encode_value(
                f'{self.previous_prefix}{value}'
                f'&page__{self._get_previous_page}')
        return None

    def _build_uri(self, encoded_value=None) -> Union[str, None]:
        regex_result = get_regex_group('^[^?]*', str(self.request.url))
        if encoded_value is None:
            return
        new_query_params = {**self.request.query_params, 'cursor': encoded_value.decode("utf-8")}

        return f'{regex_result}?{dict_to_query_string(new_query_params)}'

    def _get_first_url(self) -> str:
        regex_result = get_regex_group('^[^?]*', str(self.request.url))
        q = {**self.request.query_params, 'limit': self.limit}
        q.pop('cursor', None)
        return f'{regex_result}?{dict_to_query_string(q)}'

    @staticmethod
    def is_ordering_model_field_negative(f_name) -> bool:
        return f_name.startswith('-')

    def _get_object_list(self) -> list[Record]:
        """Final result that will be returned as object list."""
        if self.additional_count <= self.limit:
            return self._objects
        if not self.reverse:
            return self._objects[:self.additional_count - 1]
        return self._objects[1:]

    def _prefixes_init(self):
        if 'cursor_prefixes' in self.kwargs:
            self.next_prefix, self.previous_prefix = self.kwargs['cursor_prefixes']

    def paginate_object_list(
            self,
            request,
            *args,
            **kwargs: PaginationKwargs,
    ) -> list[Record]:
        self.request = request
        self.paginate_by = request.state.paginate_by
        query_params = self.request.query_params

        self.limit = self._get_limit(query_params)
        self.kwargs = kwargs
        self._prefixes_init()
        self.cursor = query_params.get('cursor')

        self._create_model_ordering()
        self._objects = self.get_objects(self._get_query_result())
        self.object_list = self._get_object_list()

        return self.object_list

    def get_paginated_response(self, object_list) -> CursorResponse:
        return {
            'results': object_list,
            'count': self.count,
            'page_limit': self.limit,
            'first_page': self._get_first_url(),
            'next_page': self._build_uri(self._get_next_url()),
            'previous_page': self._build_uri(self._get_previous_url()),
        }


class BasePaginationLimitOffset(PaginationBase, LimitPageMixin, abc.ABC):
    """
    Returns list of objects based on request's query parameters [ limit and page ].

    Big page number slows getting query result due to how OFFSET works in sql.
    The rows skipped by an OFFSET clause still have to be computed inside the server,
    therefore a large OFFSET might be inefficient.
    """

    page: int
    limit: int
    request: Request
    paginate_by: int
    _count = None

    @abc.abstractmethod
    def _get_objects(self) -> list[Record]:
        """Get list of objects from db."""

    @abc.abstractmethod
    @cached_property
    def count(self) -> int:
        """Count objects from query."""

    @cached_property
    def total_pages(self) -> int:
        if self._count == 0:
            return 0
        return math.ceil(self._count / self.limit) - 1

    @property
    def _get_next_url(self) -> Union[str, None]:
        if not self.page < self.total_pages:
            return None
        return self._build_uri(self.page + 1)

    @property
    def _get_previous_url(self) -> Union[str, None]:
        if not self.page > 0:
            return None
        return self._build_uri(self.page - 1)

    @property
    def _get_last_url(self) -> str:
        return self._build_uri(self.total_pages)

    def _build_uri(self, new_page: int) -> str:
        # catch all until first "?" occurrence
        regex_result = get_regex_group('^[^?]*', str(self.request.url))
        new_query_params = {**self.request.query_params, 'limit': self.limit, 'page': new_page}

        return f'{regex_result}?{dict_to_query_string(new_query_params)}'

    def paginate_object_list(
            self,
            request: Request,
            *args,
            **kwargs,
    ) -> list[Record]:
        self.request = request
        self.paginate_by = request.state.paginate_by
        self._count = self.count

        self.page = self._get_page(request.query_params)
        self.limit = self._get_limit(request.query_params)

        return self._get_objects()

    def get_paginated_response(self, object_list: list[Record]) -> LimitOffsetResponse:
        return {
            'results': object_list,
            'count': len(object_list),
            'total': self._count,
            'total_pages': self.total_pages,
            'page_limit': self.limit,
            'next_page': self._get_next_url,
            'previous_page': self._get_previous_url,
            'last_page': self._get_last_url,
        }


@dataclass(config=BaseConfig)
class BasePaginatorAPI(abc.ABC):
    """
    Paginator API. Initial setup.

    Arguments:
        ** request **: fastapi Request object.
        ** strategy **: pagination strategy object
           as default: PaginationLimitOffset / AsyncPaginationLimitOffset
        ** paginate_by **: number of objects per page.
        ** kwargs **: optional params passed to strategy'/s paginate_object_list method
    """
    request: Request
    strategy: Type[PaginationBase] = None
    paginate_by: int = 100
    kwargs: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.strategy_instance: PaginationBase = self.strategy()

        if self.kwargs is None or not self.kwargs or not isinstance(self.kwargs, dict):
            self.kwargs = {
                'model': None,
                'ordering': None,
                'cursor_prefixes': None
            }

        self.request.state.paginate_by = self.paginate_by

    @abc.abstractmethod
    def _strategy_data(self) -> list[Any]:
        """Returns only list of current page objects data."""

    def strategy_response(self) -> dict[str, Any]:
        """Create and return response."""
        return self.strategy_instance.get_paginated_response(self._strategy_data)
