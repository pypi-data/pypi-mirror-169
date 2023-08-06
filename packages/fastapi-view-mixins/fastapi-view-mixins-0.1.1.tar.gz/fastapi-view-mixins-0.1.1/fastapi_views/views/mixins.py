import abc
from typing import Any, Type, TypeVar, Union

from ..pagination.core import PaginationBase
from .core import BaseRepositoryView

API_CLS = TypeVar('API_CLS', bound=BaseRepositoryView)


class BaseAPIMixin:
    """Base API mixin."""

    paginate_by: Union[int, None] = None
    """Page objects limit."""
    pagination_strategy: Union[Type[PaginationBase], None] = None
    """As default set to limit offset."""
    model: Any = None

    def __init__(self, *args, **kwargs) -> None:
        attrs = kwargs.pop('attrs', {})
        self.args = args
        self.kwargs = kwargs
        self._api = None

        for key, value in attrs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise AttributeError(f'{key} is not a valid attribute')

    @property
    def api_view(self) -> API_CLS:
        return self._api

    @api_view.setter
    def api_view(self, value):
        if not isinstance(value, BaseRepositoryView):
            raise TypeError('Invalid type of api_view.')
        self._api = value

    def get_pagination_kwargs(self) -> dict[str, Any]:
        """
        Return pagination kwargs.
        Used only in cursor pagination.
        """


class AbstractAPIMixin(BaseAPIMixin, abc.ABC):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api_view = self._get_repository()

    @abc.abstractmethod
    def _get_repository(self) -> API_CLS:
        """Get repository API cls."""


class BaseAPIListMixin(BaseAPIMixin):
    """Retrieve object list mixin."""

    def get_all(self, *args, **kwargs):
        return self.api_view.get_all(*args, **kwargs)

    def get_all_with_pagination(self, *args, **kwargs):
        return self.api_view.get_all_with_pagination(*args, **kwargs)

    def get_pagination_kwargs(self) -> dict[str, Any]:
        return {
            'model': self.model,
            'ordering': [],
            'cursor_prefixes': ['next__', 'prev__']
        }


class BaseAPIDetailMixin(BaseAPIMixin):
    """Retrieve object mixin."""

    def get_detail(self, *args, **kwargs):
        return self.api_view.get_detail(*args, **kwargs)


class BaseAPIUpdateMixin(BaseAPIMixin):
    """Update objects mixin."""

    def update_one(self, *args, **kwargs):
        return self.api_view.update_one(*args, **kwargs)


class BaseAPICreateMixin(BaseAPIMixin):
    """Post objects mixin."""

    def create(self, *args, **kwargs):
        return self.api_view.create(*args, **kwargs)


class BaseAPIDestroyMixin(BaseAPIMixin):
    """Delete objects mixin."""

    def delete(self, *args, **kwargs):
        return self.api_view.delete(*args, **kwargs)
