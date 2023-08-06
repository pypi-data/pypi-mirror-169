from typing import Optional, Type, TypedDict, TypeVar, Union

from fastapi.requests import Request
from pydantic import BaseModel
from sqlalchemy.orm import Session

Table = TypeVar("Table")
Record = TypeVar('Record')


class LimitOffsetPageParams(BaseModel):
    count: Union[int, None]
    total: Union[int, None]
    total_pages: Union[int, None]
    page_limit: Union[int, None]
    next_page: Union[str, None]
    previous_page: Union[str, None]
    last_page: Union[str, None]


class CursorPageParams(BaseModel):
    count: Union[int, None]
    page_limit: Union[int, None]
    first_page: Union[str, None]
    next_page: Union[str, None]
    previous_page: Union[str, None]


class PaginationKwargs(TypedDict):
    model: Union[Type[Table], None]
    ordering: Union[list[str], None]
    cursor_prefixes: Union[list[str], None]


class LimitOffsetResponse(TypedDict):
    results: list[Record]
    count: int
    total: int
    total_pages: int
    page_limit: int
    next_page: Optional[str]
    previous_page: Optional[str]
    last_page: str


class CursorResponse(TypedDict):
    results: list[Record]
    count: int
    page_limit: int
    first_page: str
    next_page: Optional[str]
    previous_page: Optional[str]
