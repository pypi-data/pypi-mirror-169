import datetime

import mongomock
from faker import Faker
from mongomock_motor import AsyncMongoMockClient
from sqlalchemy import text

from fastapi_views.tests._tmp_db import (
    Base,
    SimpleTestOrm,
    TestingSessionLocal,
    TestingSessionLocalAsync,
    async_engine,
    engine
)

faker = Faker()


class _PymongoBase:
    def __init__(self, count: int = 50):
        self.count = count
        self.collection = None

    def _create_random_documents(self):
        result = []
        for x in range(self.count):
            name = faker.first_name().lower()
            d = {
                'username': name,
                'email': f'{name}@example.com',
                'id': x + 1,
            }
            result.append(d)
        return result

    def create_documents(self):
        self.collection.insert_many(self._create_random_documents())


class PymongoDB(_PymongoBase):

    def __init__(self, count: int = 50):
        super().__init__(count)
        self.client = mongomock.MongoClient()
        self.db = self.client.get_database('test_db')

    def create_collection(self, name: str = 'test_collection'):
        self.db.create_collection(name)
        self.collection = getattr(self.db, name)


class MotorDB(_PymongoBase):

    def __init__(self, count: int = 50):
        super().__init__(count)
        self.client = AsyncMongoMockClient()
        self.db = self.client['test_db']
        self.collection = self.db['test_collection']

    async def create_documents(self):
        await self.collection.insert_many(self._create_random_documents())


class DatabaseSession:

    def __init__(self, number: int = 50):
        self._session = None
        self._engine = None
        self._number = number

    def init(self):
        self._engine = engine
        self._session = TestingSessionLocal()

    def create_all(self):
        Base.metadata.create_all(bind=engine)
        _now = datetime.datetime.now()
        for _id in range(0, self._number):
            t = _now + datetime.timedelta(minutes=_id)
            self._session.add(SimpleTestOrm(time_created=t))
        self._session.commit()

    def close_and_drop(self):
        self._session.close()
        Base.metadata.drop_all(bind=engine)

    @property
    def session(self):
        return self._session


class AsyncDatabaseSession:

    def __init__(self):
        self._session = None
        self._engine = None

    async def init(self):
        self._engine = async_engine
        self._session = TestingSessionLocalAsync()

    async def create_all(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            ids = ', '.join(
                map(
                    lambda x: f'({x}, "{datetime.datetime.now()}")',
                    [x for x in range(1, 16)],
                ),
            )
            insert_txt = text(f"""
                INSERT INTO test_database (id, time_created)
                VALUES {ids}
            """)
            await conn.execute(insert_txt)

    async def delete_all(self):
        async with self._engine.begin() as conn:
            await conn.execute(text('DROP TABLE test_database'))

    @property
    def session(self):
        return self._session


class DatabaseSessionSameDateTime(AsyncDatabaseSession):

    async def create_all(self):
        _now = datetime.datetime.now()
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            ids = ', '.join(
                map(
                    lambda x: f'({x}, "{_now}")',
                    [x for x in range(0, 50)],
                ),
            )
            insert_txt = text(f"""
                INSERT INTO test_database (id, time_created)
                VALUES {ids}
            """)
            await conn.execute(insert_txt)
