from typing import Any, Generic, Mapping, Union

from fastapi.requests import Request
from motor.motor_asyncio import (
    AsyncIOMotorClientSession,
    AsyncIOMotorCursor,
    AsyncIOMotorDatabase
)
from pydantic.dataclasses import dataclass
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from fastapi_views.ext.motor.core import APIErrorHandlers, BaseAPIView
from fastapi_views.ext.motor.pagination.core import async_paginate_api
from fastapi_views.ext.pymongo.sync_api import SyncAPI as PymongoAPI
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record, Table


@dataclass(config=BaseConfig)
class AsyncAPI(APIErrorHandlers, PymongoAPI, BaseAPIView, Generic[Table]):
    """Async API with default methods to get, create, update, delete objects."""

    model: str = None

    async def get_all_with_pagination(
            self,
            db: AsyncIOMotorDatabase,
            request: Request,
            session: AsyncIOMotorClientSession = None,
            **kwargs,
    ):
        """Returns multiple objects using pagination."""
        self.validate_session(session)
        self.validate_pagination(request)
        self.pagination_kwargs['collection'] = getattr(db, self.model)
        self.pagination_kwargs['statement_kwargs'] = kwargs

        paginate_response = await async_paginate_api(
            statement=self.statement,
            request=request,
            session=session,
            paginate_by=self.paginate_by,
            strategy=self.pagination_strategy,
            kwargs=self.pagination_kwargs,
        )
        return paginate_response

    def get_all(
            self,
            db: AsyncIOMotorDatabase,
            session: Union[AsyncIOMotorClientSession, None] = None,
            limit: int = 100,
            skip: int = 0,
            **kwargs,
    ) -> AsyncIOMotorCursor:
        """
        Executes mongodb find method.

        Read docs for more information.

        https://motor.readthedocs.io/en/stable/tutorial-asyncio.html#querying-for-more-than-one-document

            ** Required Arguments **
                - db: motor database instance

            ** Optional Arguments **
                - session: motor client session instance
                - limit: collection limit
                - skip: collection skip
                - kwargs: additional kwargs passed to find method
        """
        return super().get_all(db, session, limit, skip, **kwargs)

    async def get_detail(
            self,
            db: AsyncIOMotorDatabase,
            session: Union[AsyncIOMotorClientSession, None] = None,
            field_value: Any = None,
            **kwargs,
    ) -> Record:
        """
        Executes mongodb findOne method.

        Be aware in case of duplicated document, only first matched will be returned.

            ** Required Arguments **
                - db: motor database instance

            ** Optional Arguments **
                - session: motor client session instance
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} for
                                getting single object. Used only if custom statement is not
                                provided
                - kwargs: additional kwargs passed to find_one method
        """
        return await super().get_detail(db, session, field_value, **kwargs)

    async def create(
            self,
            db: AsyncIOMotorDatabase,
            document: Mapping[str, Any],
            session: Union[AsyncIOMotorClientSession, None] = None,
            **kwargs,
    ) -> InsertOneResult:
        """
        Executes mongodb insertOne method.

            ** Required Arguments **
                - db: motor database instance
                - document: json object from which is created document in database

            ** Optional Arguments **
                - session: motor client session instance
                - kwargs: additional kwargs passed to insert_one method
        """
        return await super().create(db, document, session, **kwargs)

    async def delete(
            self,
            db: AsyncIOMotorDatabase,
            field_value: Any,
            session: AsyncIOMotorClientSession = None,
            **kwargs,
    ) -> DeleteResult:
        """
        Executes mongodb deleteOne method.

            ** Required Arguments **
                - db: motor database instance
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} to delete object

            ** Optional Arguments **
                - session: motor client session instance
                - kwargs: additional kwargs passed to insert_one method
        """
        return await super().delete(db, field_value, session, **kwargs)

    async def update_one(
            self,
            db: AsyncIOMotorDatabase,
            update_doc: Mapping[str, Any],
            field_value: Any = None,
            session: AsyncIOMotorClientSession = None,
            document: Mapping[str, Any] = None,
            **kwargs,
    ) -> UpdateResult:
        """
        Executes mongodb updateOne method.

        When get_statement is given then statement's returned object is used as filter document,
        otherwise you can pass your own filter document with document argument. Last option is
        just to set pk_field and send field_value

            ** Required Arguments **
                - db: motor database instance
                - update_doc: document with data to be updated by $set

            ** Optional Arguments **
                - session: motor client session instance
                - document: json object used as a filter to find an object to update
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} for
                                updating single object
                - kwargs: additional kwargs passed to find_one method
        """
        return await super().update_one(db, update_doc, field_value, session, document, **kwargs)
