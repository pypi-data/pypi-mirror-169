"""
Since most of the tests are common for sync and async,
there will be only tested repository method calls.
"""

import pytest
import pytest_asyncio
from fastapi import HTTPException
from sqlalchemy import select

from fastapi_views.ext.sql_alchemy.async_api import AsyncAPI
from fastapi_views.ext.sql_alchemy.pagination.core import AsyncPaginationCursor
from fastapi_views.tests._db_sessions import (
    AsyncDatabaseSession,
    DatabaseSession,
    DatabaseSessionSameDateTime
)
from fastapi_views.tests._tmp_db import SimpleTestOrm

NUMBER_OF_OBJECTS = 15


@pytest_asyncio.fixture
async def async_session():
    async_db_session = AsyncDatabaseSession()
    await async_db_session.init()
    await async_db_session.create_all()
    yield async_db_session.session
    await async_db_session.session.close()
    await async_db_session.delete_all()


@pytest.fixture
def sync_session():
    db_session = DatabaseSession()
    db_session.init()
    db_session.create_all()
    yield db_session.session
    db_session.close_and_drop()


@pytest_asyncio.fixture
async def session_same_datetime():
    db_session = DatabaseSessionSameDateTime()
    await db_session.init()
    await db_session.create_all()
    yield db_session.session
    await db_session.session.close()
    await db_session.delete_all()


@pytest.fixture
def api(request):
    model, pk_field, statement = request.param
    return AsyncAPI(
        model=model,
        pk_field=pk_field,
        statement=statement,
        paginate_by=3,
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, select(SimpleTestOrm))],
    indirect=['api'],
)
async def test_get_all(async_session, api):
    """Test if returns all created objects."""
    assert len(await api.get_all(session=async_session)) == NUMBER_OF_OBJECTS
    assert await api._count(async_session, select(SimpleTestOrm)) == NUMBER_OF_OBJECTS


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, select(SimpleTestOrm))],
    indirect=['api'],
)
async def test_get_all_with_pagination_async_session(async_session, request_fixture, api):
    """Test get_all limit, offset pagination using async session."""
    request_fixture.query_params = {}
    response = await api.get_all_with_pagination(session=async_session, request=request_fixture)
    # async session creates 15 objects
    assert response['total'] == 15
    assert response['count'] == 3
    assert response['page_limit'] == 3
    assert 'results' in response
    assert 'next_page' in response
    assert 'previous_page' in response
    assert 'last_page' in response

    assert type(response['results']) == list
    assert len(response['results']) == response['count']


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, select(SimpleTestOrm))],
    indirect=['api'],
)
async def test_get_all_with_pagination_sync_session(sync_session, request_fixture, api):
    """Test get_all limit, offset pagination using sync session."""
    with pytest.raises(TypeError):
        await api.get_all_with_pagination(session=sync_session, request=request_fixture)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, select(SimpleTestOrm).where(SimpleTestOrm.id > 43))],
    indirect=['api'],
)
async def test_get_all_with_pagination_cursor(session_same_datetime, request_fixture, api):
    """Test get_all cursor pagination using sync session."""
    request_fixture.query_params = {}
    api.pagination_kwargs = {
        'model': SimpleTestOrm,
        'ordering': ['-time_created'],
        'cursor_prefixes': ['next__', 'prev__']
    }
    api.pagination_strategy = AsyncPaginationCursor
    api.paginate_by = 6
    response = await api.get_all_with_pagination(
        session=session_same_datetime,
        request=request_fixture,
    )
    assert response['results'][0].id == 44


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, select(SimpleTestOrm).where(SimpleTestOrm.id > 43))],
    indirect=['api'],
)
async def test_get_all_with_pagination_cursor_2(session_same_datetime, request_fixture, api):
    """Test get_all cursor pagination using sync session with two ordering fields."""
    request_fixture.query_params = {}
    api.pagination_kwargs = {
        'model': SimpleTestOrm,
        'ordering': ['-time_created', '-id'],
        'cursor_prefixes': ['next__', 'prev__']
    }
    api.pagination_strategy = AsyncPaginationCursor
    api.paginate_by = 6
    response = await api.get_all_with_pagination(
        session=session_same_datetime,
        request=request_fixture,
    )
    assert response['results'][0].id == 49


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, 'id', None)],
    indirect=['api'],
)
async def test_get_detail(async_session, api):
    """Test get_detail method."""
    result = await api.get_detail(async_session, field_value=2)
    assert result.id == 2
    assert type(result).__name__ == 'SimpleTestOrm'

    api.statement = select(SimpleTestOrm).where(
        SimpleTestOrm.id == 5,
    )
    result = await api.get_detail(async_session)
    assert result.id == 5

    api.statement = select(SimpleTestOrm)
    with pytest.raises(ValueError):
        await api.get_detail(async_session)

    api.statement = None
    with pytest.raises(HTTPException):
        await api.get_detail(
            session=async_session,
            field_value=17,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, None)],
    indirect=['api'],
)
async def test_create(async_session, api):
    """Test create method."""
    result = await api.create(
        session=async_session
    )
    assert result.id > NUMBER_OF_OBJECTS
    assert type(result).__name__ == 'SimpleTestOrm'

    with pytest.raises(HTTPException):
        await api.create(
            session=async_session,
            data={
                'id': 'invalid'
            }
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, 'id', None)],
    indirect=['api'],
)
async def test_delete(async_session, api):
    """Test delete method."""
    assert await api._count(async_session, select(SimpleTestOrm)) == NUMBER_OF_OBJECTS
    await api.delete(
        session=async_session,
        field_value=13,
    )
    with pytest.raises(HTTPException):
        await api.get_detail(async_session, 13)

    assert await api._count(async_session, select(SimpleTestOrm)) == NUMBER_OF_OBJECTS - 1


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, None, None)],
    indirect=['api'],
)
async def test_delete_pk_field_error(async_session, api):
    """Test delete method pk_field error."""
    with pytest.raises(AttributeError):
        await api.delete(
            session=async_session,
            field_value=13,
        )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, 'id', None)],
    indirect=['api'],
)
async def test_update_one(async_session, api):
    """Test update_one method."""
    await api.update_one(
        session=async_session,
        field_value=1,
        data={
            'id': 100
        }
    )
    assert await api.get_detail(async_session, 100) is not None
    with pytest.raises(HTTPException):
        await api.get_detail(async_session, 1)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'api',
    [(SimpleTestOrm, 'id', None)],
    indirect=['api'],
)
async def test_update_one_attrs(async_session, api):
    """Test update_one method attrs."""
    with pytest.raises(TypeError):
        await api.update_one()
    with pytest.raises(AttributeError):
        await api.update_one(session=None, field_value=2)

    with pytest.raises(TypeError):
        await api.update_one(session='not_valid_type', field_value=2)

    with pytest.raises(HTTPException):
        await api.update_one(session=async_session, field_value=2)

    api.pk_field = None
    with pytest.raises(AttributeError):
        await api.update_one(session=async_session, field_value=2, data={'id': 100})

    api.pk_field = 'id'
    with pytest.raises(HTTPException):
        await api.update_one(session=async_session, field_value=2, data={'id': 'invalid'})
