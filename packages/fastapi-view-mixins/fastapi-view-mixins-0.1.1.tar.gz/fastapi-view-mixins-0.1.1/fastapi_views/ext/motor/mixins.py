from typing import TypeVar

from fastapi_views.ext.pymongo.mixins import \
    APICreateMixin as PymongoAPICreateMixin
from fastapi_views.ext.pymongo.mixins import \
    APIDestroyMixin as PymongoAPIDestroyMixin
from fastapi_views.ext.pymongo.mixins import \
    APIDetailMixin as PymongoAPIDetailMixin
from fastapi_views.ext.pymongo.mixins import \
    APIListMixin as PymongoAPIListMixin
from fastapi_views.ext.pymongo.mixins import APIMixin as PymongoAPIMixin
from fastapi_views.ext.pymongo.mixins import \
    APIUpdateMixin as PymongoAPIUpdateMixin

from ...views.core import BaseRepositoryView
from .async_api import AsyncAPI

API_CLS = TypeVar('API_CLS', bound=BaseRepositoryView)


class APIMixin(PymongoAPIMixin):
    """
    Base API mixin.

        ** Required Arguments **
            - model: name of the collection

        ** Optional Arguments **
            - pk_field: unique field like collection id
            - paginate_by: number of returned objects per page
            - pagination_strategy: AsyncPaginationLimitOffset ( default ) / AsyncPaginationCursor

    You can override get_statement and get_pagination_kwargs methods

    Examples:
            def get_pagination_kwargs(self) -> dict[str, Any]:
                kw = super().get_pagination_kwargs()
                kw['ordering'] = ['id']
                return kw

            def get_statement(self) -> Mapping[str, Any]:
                return {'name': 'john', 'age': {'$gt': 25}}
    """

    @property
    def _async_instance(self) -> AsyncAPI:
        return AsyncAPI[self.model](**self._repository_kwargs)

    def _get_repository(self) -> API_CLS:
        """Get repository API cls."""
        return self._async_instance


class APIListMixin(APIMixin, PymongoAPIListMixin):
    """Retrieve object list mixin."""


class APIDetailMixin(APIMixin, PymongoAPIDetailMixin):
    """Retrieve object mixin."""


class APIUpdateMixin(APIMixin, PymongoAPIUpdateMixin):
    """Update objects mixin."""


class APICreateMixin(APIMixin, PymongoAPICreateMixin):
    """Post objects mixin."""


class APIDestroyMixin(APIMixin, PymongoAPIDestroyMixin):
    """Delete objects mixin."""
