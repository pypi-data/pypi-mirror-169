import abc
from typing import Any, Generic, Type, Union

from fastapi import HTTPException, status
from fastapi.requests import Request
from pydantic import validator
from pydantic.dataclasses import dataclass

from fastapi_views.pagination.core import BasePaginationCursor, PaginationBase
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Table


class RepositoryExceptions:

    def __init__(self, model: Type[Table]):
        self.model = model

    def attribute_error(self, field_name: str) -> None:
        raise AttributeError(f'{field_name} is required.')

    def request_type_error(self) -> None:
        raise TypeError('Request must be type of fastapi.requests Request.')

    def validate_request(self, request) -> None:
        if request is None:
            self.attribute_error('request')
        if not isinstance(request, Request):
            self.request_type_error()

    def not_found_exception(self, unique: Any):
        """Object not found exception."""
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{self.model.__name__} with <{type(unique)}:{unique}> does not exist.'
        )

    @staticmethod
    def integrity_error(error):
        """Integrity exception."""
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error,
        )

    @staticmethod
    def empty_update_error():
        """Integrity exception."""
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Nothing to update.',
        )


@dataclass(config=BaseConfig)
class BaseRepositoryView(Generic[Table], abc.ABC):
    """Base repository API class."""

    model: Type[Table] = None
    paginate_by: int = None
    pagination_strategy: Type[PaginationBase] = None
    pagination_kwargs: Union[dict[str, Any], None] = None

    def __post_init__(self):
        self.exceptions = RepositoryExceptions(model=self.model)

    @validator('model')
    def model_can_not_be_empty(cls, value: Table):
        """Model field validator."""
        if not value or value is None:
            raise ValueError('Model field is required.')
        return value

    def validate_pagination(self, request):
        if self.pagination_strategy and issubclass(self.pagination_strategy, BasePaginationCursor):
            if not self.pagination_kwargs['ordering']:
                raise ValueError('At least one ordering field is required.')
        self.exceptions.validate_request(request)
        if self.paginate_by is None:
            self.exceptions.attribute_error('paginate_by')
        if not isinstance(self.paginate_by, int) or isinstance(self.paginate_by, bool):
            raise TypeError('paginate_by must be type of int')
        if self.paginate_by <= 0:
            raise ValueError('paginate_by value should be higher than 0')

    @abc.abstractmethod
    def get_all(self, *args, **kwargs):
        """Returns multiple objects."""

    @abc.abstractmethod
    def get_detail(self, *args, **kwargs):
        """Return single object."""

    @abc.abstractmethod
    def create(self, *args, **kwargs):
        """Perform object creation."""

    @abc.abstractmethod
    def delete(self, *args, **kwargs):
        """Remove object."""

    @abc.abstractmethod
    def update_one(self, *args, **kwargs):
        """Perform single object update."""
