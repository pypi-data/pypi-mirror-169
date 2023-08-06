from typing import Awaitable
from unittest.mock import patch

import pytest
import pytest_asyncio

from fastapi_views.ext.motor.pagination.core import (
    AsyncPaginationCursor,
    AsyncPaginationLimitOffset,
    AsyncPaginatorAPI,
    async_paginate_api
)
from fastapi_views.pagination.annotations import CursorResponse
from fastapi_views.utils import encode_value


@pytest_asyncio.fixture
async def async_limit_offset_api(request_fixture, request, motor_collection) -> dict:
    request_fixture.query_params = {
        'page': request.param,
        'limit': 3,
    }
    return await async_paginate_api(
        statement={},
        request=request_fixture,
        kwargs={
            'collection': motor_collection
        }
    )


@pytest_asyncio.fixture
@patch('fastapi_views.ext.motor.pagination.core.AsyncPaginationCursor._filter_query')
async def async_cursor_api(q, request_fixture, request, motor_collection) -> Awaitable[dict]:
    cursor, ordering, operator_expr, operator_value = request.param

    if cursor is not None:
        q.return_value = motor_collection.find(
            {'$expr': {f'${operator_expr}': ['$id', operator_value]}}
        )
    request_fixture.query_params = {
        'limit': 2,
        'cursor': cursor,
    }
    return await async_paginate_api(
        statement={},
        request=request_fixture,
        strategy=AsyncPaginationCursor,
        kwargs={
            'model': 'test_collection',
            'ordering': ordering,
            'cursor_prefixes': ['custom_next__', 'custom_prev__'],
            'collection': motor_collection
        }
    )


class TestPaginatorAPI:

    @patch('fastapi_views.ext.motor.pagination.core.AsyncPaginatorAPI.strategy_response')
    def test_init(self, response_mock, request_fixture):
        """Test if values are initialized as expected."""
        response_mock.return_value = {}

        paginator = AsyncPaginatorAPI(
            statement={},
            request=request_fixture,
            paginate_by=5
        )
        assert paginator.statement is not None
        assert paginator.request is not None
        assert paginator.session is None
        assert paginator.strategy is not None
        assert paginator.paginate_by is not None
        assert paginator.strategy == AsyncPaginationLimitOffset
        assert paginator.paginate_by == 5
        assert paginator.kwargs == {
            'model': None,
            'ordering': None,
            'cursor_prefixes': None,
        }


@pytest.mark.asyncio
class TestLimitOffset:

    @pytest.mark.parametrize(
        'async_limit_offset_api',
        [0, 1, 2, 3, 16],
        indirect=['async_limit_offset_api'],
    )
    async def test_strategy_response_common(
            self,
            async_limit_offset_api: dict,
    ):
        """Test pagination response the same common values in every page."""
        assert async_limit_offset_api['total'] == 50
        assert async_limit_offset_api['total_pages'] == 16
        assert async_limit_offset_api['page_limit'] == 3

    @pytest.mark.parametrize('async_limit_offset_api', [0], indirect=['async_limit_offset_api'])
    async def test_strategy_response(self, async_limit_offset_api: dict):
        """Test pagination response starting at page 0."""
        assert async_limit_offset_api['count'] == 3
        assert async_limit_offset_api['next_page'] == 'https://example.com?page=1&limit=3'
        assert async_limit_offset_api['previous_page'] is None
        assert async_limit_offset_api['last_page'] == 'https://example.com?page=16&limit=3'

    @pytest.mark.parametrize('async_limit_offset_api', [1], indirect=['async_limit_offset_api'])
    async def test_strategy_response_1(self, async_limit_offset_api: dict):
        """Test pagination response starting at page 1."""
        assert async_limit_offset_api['count'] == 3
        assert async_limit_offset_api['next_page'] == 'https://example.com?page=2&limit=3'
        assert async_limit_offset_api['previous_page'] == 'https://example.com?page=0&limit=3'
        assert async_limit_offset_api['last_page'] == 'https://example.com?page=16&limit=3'

    @pytest.mark.parametrize('async_limit_offset_api', [16], indirect=['async_limit_offset_api'])
    async def test_strategy_response_last(self, async_limit_offset_api: dict):
        """Test pagination response starting in last page."""
        assert async_limit_offset_api['count'] == 2
        assert async_limit_offset_api['next_page'] is None
        assert async_limit_offset_api['previous_page'] == 'https://example.com?page=15&limit=3'
        assert async_limit_offset_api['last_page'] == 'https://example.com?page=16&limit=3'


cursor_to_load_last_page = encode_value('custom_next__48&page__16').decode("utf-8")
cursor_to_load_last_page_reverse = encode_value('custom_next__3&page__4').decode("utf-8")


def assert_result(result: CursorResponse, next_cursor=None, prev_cursor=None):
    """
    Count is the same for all results because in our test we have 10 objects,
    which paginated by 2 gives equal number of objects per page.
    """
    assert result['count'] == 2
    assert result['page_limit'] == 2
    assert result['first_page'] == 'https://example.com?limit=2'
    if next_cursor is not None:
        next_page_url = f'https://example.com?limit=2&cursor={next_cursor.decode("utf-8")}'
        assert result['next_page'] == next_page_url
    else:
        assert result['next_page'] is None

    if prev_cursor is not None:
        prev_url = f'https://example.com?limit=2&cursor={prev_cursor.decode("utf-8")}'
        assert result['previous_page'] == prev_url
    else:
        assert result['previous_page'] is None


class TestCursorAscendingOrder:
    """We assume in tests that we have 50 objects ordered by id paginated by 2."""

    @staticmethod
    def _get_doc_id(doc: dict):
        return doc.get('id')

    @staticmethod
    def assert_common(result):
        assert result['count'] == 2
        assert result['page_limit'] == 2
        assert result['first_page'] == 'https://example.com?limit=2'

    @pytest.mark.parametrize(
        'async_cursor_api',
        [(None, ['id'], None, None)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response(self, async_cursor_api):
        """Test pagination response."""
        next_page_cursor = encode_value('custom_next__2&page__1')
        assert_result(async_cursor_api, next_page_cursor)
        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [1, 2]

    @pytest.mark.parametrize(
        'async_cursor_api',
        [('Y3VzdG9tX25leHRfXzImcGFnZV9fMQ==', ['id'], 'gt', 2)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response_with_cursor(self, async_cursor_api: dict):
        """Test pagination response 'at page 1'."""
        next_page_cursor = encode_value('custom_next__4&page__2')
        previous_page_cursor = encode_value('custom_prev__3&page__0')
        assert_result(async_cursor_api, next_page_cursor, previous_page_cursor)
        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [3, 4]

    @pytest.mark.parametrize(
        'async_cursor_api',
        [(cursor_to_load_last_page, ['id'], 'gt', 48)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response_with_cursor_last_page(self, async_cursor_api: dict):
        """Test pagination response 'in last page'."""
        previous_page_cursor = encode_value('custom_prev__49&page__15')
        assert_result(async_cursor_api, prev_cursor=previous_page_cursor)

        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [49, 50]


class TestCursorDescendingOrder:
    """We assume in tests that we have 50 objects ordered by id desc paginated by 2."""

    @staticmethod
    def _get_doc_id(doc: dict):
        return doc.get('id')

    @pytest.mark.parametrize(
        'async_cursor_api',
        [(None, ['-id'], None, None)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response(self, async_cursor_api: dict):
        """Test pagination response."""
        next_page_cursor = encode_value('custom_next__49&page__1')
        assert_result(async_cursor_api, next_page_cursor)

        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [50, 49]

    @pytest.mark.parametrize(
        'async_cursor_api',
        [('Y3VzdG9tX25leHRfXzkmcGFnZV9fMQ==', ['-id'], 'lt', 49)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response_with_cursor(self, async_cursor_api: dict):
        """Test pagination response 'at page 1'."""
        next_page_cursor = encode_value('custom_next__47&page__2')
        previous_page_cursor = encode_value('custom_prev__48&page__0')
        assert_result(async_cursor_api, next_page_cursor, previous_page_cursor)

        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [48, 47]

    @pytest.mark.parametrize(
        'async_cursor_api',
        [(cursor_to_load_last_page_reverse, ['-id'], 'lt', 3)],
        indirect=['async_cursor_api'],
    )
    def test_strategy_response_with_cursor_last_page(self, async_cursor_api: dict):
        """Test pagination response 'in last page'."""
        previous_page_cursor = encode_value('custom_prev__2&page__3')
        assert_result(async_cursor_api, prev_cursor=previous_page_cursor)

        api_ids = list(map(self._get_doc_id, async_cursor_api['results']))
        assert api_ids == [2, 1]
