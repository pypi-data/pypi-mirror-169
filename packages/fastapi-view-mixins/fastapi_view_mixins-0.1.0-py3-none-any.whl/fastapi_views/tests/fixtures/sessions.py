from unittest.mock import MagicMock

import pytest
import pytest_asyncio
from motor.motor_asyncio import AsyncIOMotorClientSession
from pymongo.client_session import ClientSession

from fastapi_views.tests._db_sessions import MotorDB, PymongoDB


@pytest.fixture
def pymongo_database():
    _db = PymongoDB()
    _db.create_collection('test_collection')
    _db.create_documents()

    yield _db.db


@pytest_asyncio.fixture
async def motor_collection():
    _db = MotorDB()
    await _db.create_documents()

    yield _db.collection


@pytest_asyncio.fixture
async def motor_database():
    _db = MotorDB()
    await _db.create_documents()

    yield _db.db


@pytest.fixture()
def client_session():
    class SessionMock:
        pass

    return MagicMock(spec=ClientSession, return_value=SessionMock())


@pytest.fixture()
def motor_client_session():
    class SessionMock:
        pass

    return MagicMock(spec=AsyncIOMotorClientSession, return_value=SessionMock())
