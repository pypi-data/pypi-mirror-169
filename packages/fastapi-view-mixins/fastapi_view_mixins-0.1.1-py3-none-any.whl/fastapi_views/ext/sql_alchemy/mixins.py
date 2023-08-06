from functools import cached_property
from typing import Any, Type, TypeVar, Union

from sqlalchemy import select
from sqlalchemy.sql import Select

from fastapi_views.ext.sql_alchemy.async_api import AsyncAPI
from fastapi_views.ext.sql_alchemy.sync_api import SyncAPI

from ...types import Table
from ...views.mixins import (
    AbstractAPIMixin,
    BaseAPICreateMixin,
    BaseAPIDestroyMixin,
    BaseAPIDetailMixin,
    BaseAPIListMixin,
    BaseAPIUpdateMixin
)
from .core import BaseAPIView

API_CLS = TypeVar('API_CLS', bound=BaseAPIView)


class APIMixin(AbstractAPIMixin):
    """Base API mixin."""

    model: Type[Table] = None
    """A database table model class."""
    pk_field: Union[str, None] = None
    """Unique field like model id."""
    async_api: bool = False
    """When set to True then will be used async repository."""

    @cached_property
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

    @property
    def _async_instance(self) -> AsyncAPI:
        return AsyncAPI[self.model](**self._repository_kwargs)

    def _get_repository(self) -> API_CLS:
        """Get repository API cls."""
        return self._sync_instance if not self.async_api else self._async_instance

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if not isinstance(self.async_api, bool):
            raise TypeError(f'{self.async_api} expected to be boolean value.')

        # assigned after, so we can reference to api_view in both of the methods if needed
        self.api_view.pagination_kwargs = self.get_pagination_kwargs()
        self.api_view.statement = self.get_statement()

    def get_statement(self) -> Select:
        """Return sqlalchemy orm statement."""


class APIListMixin(APIMixin, BaseAPIListMixin):
    """Retrieve object list mixin."""

    pk_field = None

    def get_statement(self) -> Select:
        return select(self.model)

    def get_pagination_kwargs(self) -> dict[str, Any]:
        kw = super().get_pagination_kwargs()
        kw['ordering'] = ['id']
        return kw


class APIDetailMixin(APIMixin, BaseAPIDetailMixin):
    """Retrieve object mixin."""

    pk_field = 'id'


class APIUpdateMixin(APIMixin, BaseAPIUpdateMixin):
    """Update objects mixin."""

    pk_field = 'id'


class APICreateMixin(APIMixin, BaseAPICreateMixin):
    """Post objects mixin."""

    pk_field = None


class APIDestroyMixin(APIMixin, BaseAPIDestroyMixin):
    """Delete objects mixin."""

    pk_field = 'id'
