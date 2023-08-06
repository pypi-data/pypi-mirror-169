from typing import Any, Mapping, TypeVar, Union

from fastapi_views.ext.pymongo.sync_api import SyncAPI

from ...views.core import BaseRepositoryView
from ...views.mixins import (
    AbstractAPIMixin,
    BaseAPICreateMixin,
    BaseAPIDestroyMixin,
    BaseAPIDetailMixin,
    BaseAPIListMixin,
    BaseAPIUpdateMixin
)

API_CLS = TypeVar('API_CLS', bound=BaseRepositoryView)


class APIMixin(AbstractAPIMixin):
    """
    Base API mixin.

        ** Required Arguments **
            - model: name of the collection

        ** Optional Arguments **
            - pk_field: unique field like collection id
            - paginate_by: number of returned objects per page
            - pagination_strategy: PaginationLimitOffset ( default ) / PaginationCursor

    You can override get_statement and get_pagination_kwargs methods

    Examples:
            def get_pagination_kwargs(self) -> dict[str, Any]:
                kw = super().get_pagination_kwargs()
                kw['ordering'] = ['id']
                return kw

            def get_statement(self) -> Mapping[str, Any]:
                return {'name': 'john', 'age': {'$gt': 25}}
    """

    model: str = None
    """Name of the collection."""
    pk_field: Union[str, None] = None
    """Unique field like model id."""

    @property
    def _repository_kwargs(self) -> dict:
        return dict(
            model=self.model,
            pk_field=self.pk_field,
            paginate_by=self.paginate_by,
            pagination_strategy=self.pagination_strategy,
        )

    @property
    def _sync_instance(self) -> SyncAPI:
        return SyncAPI[self.model](**self._repository_kwargs)

    def _get_repository(self) -> API_CLS:
        """Get repository API cls."""
        return self._sync_instance

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # assigned after, so we can reference to api_view in both of the methods if needed
        self.api_view.pagination_kwargs = self.get_pagination_kwargs()
        self.api_view.statement = self.get_statement()

    def get_statement(self) -> Mapping[str, Any]:
        """Return mongodb raw statement."""


class APIListMixin(APIMixin, BaseAPIListMixin):
    """Retrieve object list mixin."""

    pk_field = None

    def get_statement(self) -> Mapping[str, Any]:
        return {}


class APIDetailMixin(APIMixin, BaseAPIDetailMixin):
    """Retrieve object mixin."""

    pk_field = '_id'


class APIUpdateMixin(APIMixin, BaseAPIUpdateMixin):
    """Update objects mixin."""

    pk_field = '_id'


class APICreateMixin(APIMixin, BaseAPICreateMixin):
    """Post objects mixin."""

    pk_field = None


class APIDestroyMixin(APIMixin, BaseAPIDestroyMixin):
    """Delete objects mixin."""

    pk_field = '_id'
