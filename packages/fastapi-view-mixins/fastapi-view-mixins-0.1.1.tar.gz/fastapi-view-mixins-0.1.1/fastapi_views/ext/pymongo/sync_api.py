from typing import Any, Generic, Mapping, Union

from bson import InvalidDocument
from motor.motor_asyncio import (
    AsyncIOMotorClientSession,
    AsyncIOMotorCursor,
    AsyncIOMotorDatabase
)
from pydantic.dataclasses import dataclass
from pymongo.client_session import ClientSession
from pymongo.cursor import Cursor
from pymongo.database import Database
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from fastapi_views.ext.pymongo.core import BaseAPIView
from fastapi_views.settings import BaseConfig
from fastapi_views.types import Record, Table


@dataclass(config=BaseConfig)
class SyncAPI(BaseAPIView, Generic[Table]):
    """
    Sync API with default methods to get, create, update, delete objects.

    Motor types shown in Union's are only provided for readability when called by motor methods.
    """
    model: str = None  # collection name

    def get_all(
            self,
            db: Union[AsyncIOMotorDatabase, Database],
            session: Union[AsyncIOMotorClientSession, ClientSession, None] = None,
            limit: int = 100,
            skip: int = 0,
            **kwargs,
    ) -> Union[AsyncIOMotorCursor, Cursor]:
        """
        Executes mongodb find method.

        Read docs for more information.

            ** Required Arguments **
                - db: motor / pymongo database instance

            ** Optional Arguments **
                - session: motor / pymongo client session instance
                - limit: collection limit
                - skip: collection skip
                - kwargs: additional kwargs passed to find method
        """
        self.validate_session(session)
        self.validate_statement()
        collection = self._get_collection(db)
        return collection.find(self.statement, session=session, **kwargs).limit(limit).skip(skip)

    def _get_detail_statement(self, field_value) -> Mapping[str, Any]:
        if self.statement is not None:
            return self.statement
        self.validate_field_value(field_value)
        if self.pk_field is None:
            self.exceptions.attribute_error('pk_field')
        return {self.pk_field: field_value}

    def get_detail(
            self,
            db: Union[AsyncIOMotorDatabase, Database],
            session: Union[AsyncIOMotorClientSession, ClientSession, None] = None,
            field_value: Any = None,
            **kwargs,
    ) -> Record:
        """
        Executes mongodb findOne method.

        Be aware in case of duplicated document, only first matched will be returned.

            ** Required Arguments **
                - db: motor / pymongo database instance

            ** Optional Arguments **
                - session: motor / pymongo client session instance
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} for
                                getting single object. Used only if custom statement is not
                                provided
                - kwargs: additional kwargs passed to find_one method
        """
        self.validate_session(session)
        statement = self._get_detail_statement(field_value)
        collection = self._get_collection(db)
        result = collection.find_one(statement, session=session, **kwargs)
        if result is None:
            self.not_found_exception(field_value)
        return result

    def create(
            self,
            db: Union[AsyncIOMotorDatabase, Database],
            document: Mapping[str, Any],
            session: Union[AsyncIOMotorClientSession, ClientSession, None] = None,
            **kwargs,
    ) -> InsertOneResult:
        """
        Executes mongodb insertOne method.

            ** Required Arguments **
                - db: motor / pymongo database instance
                - document: json object from which is created document in database

            ** Optional Arguments **
                - session: motor / pymongo client session instance
                - kwargs: additional kwargs passed to insert_one method
        """
        self.validate_session(session)
        if not isinstance(document, dict):
            raise TypeError('Document is expected to be type of dict')

        return self._get_collection(db).insert_one(document, session=session, **kwargs)

    def delete(
            self,
            db: Union[AsyncIOMotorDatabase, Database],
            field_value: Any,
            session: Union[AsyncIOMotorClientSession, ClientSession, None] = None,
            **kwargs,
    ) -> DeleteResult:
        """
        Executes mongodb deleteOne method.

            ** Required Arguments **
                - db: motor / pymongo database instance
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} to delete object

            ** Optional Arguments **
                - session: motor / pymongo client session instance
                - kwargs: additional kwargs passed to insert_one method
        """
        self.validate_session(session)
        self.validate_field_value(field_value)

        collection = self._get_collection(db)
        try:
            if self.pk_field is None:
                self.exceptions.attribute_error('pk_field')
            return collection.delete_one({self.pk_field: field_value}, session=session, **kwargs)
        except (TypeError, InvalidDocument) as e:
            self.invalid_document(str(e))

    def _get_collection(self, db):
        return getattr(db, self.model)

    def _create_update_doc(
            self,
            field_value: Any = None,
            document: Mapping[str, Any] = None,
    ):
        if self.statement is not None:
            return self.statement
        if self.pk_field is None and document is None:
            raise AttributeError('pk_field or document has to be provided.')
        if self.pk_field is None or not self.pk_field:
            self.exceptions.attribute_error('pk_field')
        self.validate_field_value(field_value)
        return {self.pk_field: field_value}

    def update_one(
            self,
            db: Union[AsyncIOMotorDatabase, Database],
            update_doc: Mapping[str, Any],
            field_value: Any = None,
            session: Union[AsyncIOMotorClientSession, ClientSession, None] = None,
            document: Mapping[str, Any] = None,
            **kwargs,
    ) -> UpdateResult:
        """
        Executes mongodb updateOne method.

        When get_statement is given then statement's returned object is used as filter document,
        otherwise you can pass your own filter document with document argument. Last option is
        just to set pk_field and send field_value

            ** Required Arguments **
                - db: motor / pymongo database instance
                - update_doc: document with data to be updated by $set

            ** Optional Arguments **
                - session: motor / pymongo client session instance
                - document: json object used as a filter to find an object to update
                - field_value: should be a unique value that will be used to create
                                filter document like {self.pk_field: field_value} for
                                updating single object
                - kwargs: additional kwargs passed to find_one method
        """
        self.validate_session(session)
        if document is None:
            document = self._create_update_doc(field_value, document)

        collection = self._get_collection(db)
        return collection.update_one(document, {"$set": update_doc}, session=session, **kwargs)
