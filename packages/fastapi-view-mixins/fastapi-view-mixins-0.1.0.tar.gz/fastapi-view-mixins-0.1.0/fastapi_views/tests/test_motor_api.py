import pytest
from fastapi.exceptions import HTTPException

from fastapi_views.ext.motor.async_api import AsyncAPI
from fastapi_views.ext.motor.pagination.core import AsyncPaginationCursor

NUMBER_OF_OBJECTS = 50  # number of objects created by sync db


@pytest.fixture
def motor_api(request):
    collection, pk_field, paginate_by, strategy, kwargs, statement = request.param
    return AsyncAPI(
        model=collection,
        pk_field=pk_field,
        paginate_by=paginate_by,
        pagination_strategy=strategy,
        pagination_kwargs=kwargs,
        statement=statement,
    )


class TestAsyncAPI:
    """Test motor api cls."""

    @pytest.mark.parametrize('test_input', [None, ''])
    def test_init_model_raise_value_error(self, test_input):
        """Test collection value error."""
        with pytest.raises(ValueError):
            assert AsyncAPI(model=test_input)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    def test_session_get_all_raises(self, motor_api: AsyncAPI):
        """Test session attr in get_all method."""
        with pytest.raises(TypeError):
            motor_api.get_all(db=None, session=False)
        with pytest.raises(TypeError):
            motor_api.get_all(db=None, session=True)
        with pytest.raises(TypeError):
            motor_api.get_all(db=None, session='foo_str')


@pytest.mark.asyncio
class TestAsyncWithAsyncioMark:

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_session_get_detail_raises(self, motor_api: AsyncAPI):
        """Test session attr in get_detail method."""
        with pytest.raises(TypeError):
            await motor_api.get_detail(db=None, session=False)
        with pytest.raises(TypeError):
            await motor_api.get_detail(db=None, session=True)
        with pytest.raises(TypeError):
            await motor_api.get_detail(db=None, session='foo_str')

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_session_update_one_raises(self, motor_api: AsyncAPI):
        """Test session attr in update_one method."""
        with pytest.raises(TypeError):
            await motor_api.update_one(db=None, session=False)
        with pytest.raises(TypeError):
            await motor_api.update_one(db=None, session=True)
        with pytest.raises(TypeError):
            await motor_api.update_one(db=None, session='foo_str', update_doc={})

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_session_create_raises(self, motor_api: AsyncAPI):
        """Test session attr in create method."""
        with pytest.raises(TypeError):
            await motor_api.create(db=None, session=False, document={})
        with pytest.raises(TypeError):
            await motor_api.create(db=None, session=True, document={})
        with pytest.raises(TypeError):
            await motor_api.create(db=None, session='foo_str', document={})

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_session_delete_raises(self, motor_api: AsyncAPI):
        """Test session attr in delete method."""
        with pytest.raises(TypeError):
            await motor_api.delete(db=None, session=False, field_value=None)
        with pytest.raises(TypeError):
            await motor_api.delete(db=None, session=True, field_value=None)
        with pytest.raises(TypeError):
            await motor_api.delete(db=None, session='foo_str', field_value=None)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_get_all_statement_raises(self, motor_api: AsyncAPI):
        """Test statement attr in get_all method."""
        with pytest.raises(TypeError):
            class Cls:
                pass

            await motor_api.get_all(db=None, session=Cls)
        with pytest.raises(TypeError):
            await motor_api.get_all(db=None, session=False)
        with pytest.raises(TypeError):
            await motor_api.get_all(db=None, session=True)
        with pytest.raises(TypeError):
            await motor_api.get_all(db=None, session='foo_str')
        with pytest.raises(TypeError):
            await motor_api.get_all(db=None, session=2)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, {})],
        indirect=['motor_api'],
    )
    async def test_session_get_methods(
            self,
            motor_api: AsyncAPI,
            motor_database,
            motor_client_session,
    ):
        """Test session correct type. In some cases session is not implemented in mongomock yet."""
        assert motor_api.get_all(db=motor_database, session=motor_client_session)
        assert await motor_api.get_detail(db=motor_database, session=motor_client_session)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, {})],
        indirect=['motor_api'],
    )
    async def test_get_all(self, motor_api: AsyncAPI, motor_database, motor_client_session):
        """Test get_all method."""
        response = motor_api.get_all(db=motor_database, session=motor_client_session)
        assert len(await response.to_list()) == NUMBER_OF_OBJECTS
        response = motor_api.get_all(db=motor_database, session=motor_client_session, limit=10)
        assert len(await response.to_list()) == 10
        response = motor_api.get_all(
            db=motor_database,
            session=motor_client_session,
            limit=5,
            skip=5,
        )
        response_list = await response.to_list()
        assert response_list[0]['id'] == 6  # first 5 result skipped
        assert len(response_list) == 5  # limit value

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_get_detail(self, motor_api: AsyncAPI, motor_database):
        """Test get_detail method with id as pk_field."""
        response = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        assert response['id'] == 1

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_get_detail_pk_field(self, motor_api: AsyncAPI, motor_database):
        """Test get_detail method with None as pk_field."""
        with pytest.raises(AttributeError):
            await motor_api.get_detail(
                db=motor_database,
                field_value=1,
            )

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, {'id': 15})],
        indirect=['motor_api'],
    )
    async def test_get_detail_statement(self, motor_api: AsyncAPI, motor_database):
        """Test get_detail method with None as pk_field and custom statement."""
        response = await motor_api.get_detail(
            db=motor_database,
        )
        assert response['id'] == 15

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_get_detail_not_found(self, motor_api: AsyncAPI, motor_database):
        """Test get_detail method not found."""
        assert await motor_api.get_detail(
            db=motor_database,
            field_value=51,
        ) is None

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_create(self, motor_api: AsyncAPI, motor_database):
        """Test create method."""
        new_doc = {'username': 'john', 'age': 22, 'id': 111}
        await motor_api.create(
            db=motor_database,
            document=new_doc,
        )
        latest = await motor_api.get_detail(
            db=motor_database,
            field_value=new_doc['id'],
        )
        assert latest['username'] == 'john'
        assert latest['age'] == 22

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_create_invalid_document(self, motor_api: AsyncAPI, motor_database):
        """Test create method invalid document."""
        new_doc = False
        with pytest.raises(TypeError):
            await motor_api.create(
                db=motor_database,
                document=new_doc,
            )

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_update_one_doc_none(self, motor_api: AsyncAPI, motor_database):
        """Test update_one method document none."""
        first = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        first_username = first['username']
        assert first_username != 'new_username'
        # update first
        await motor_api.update_one(
            db=motor_database,
            field_value=1,
            update_doc={'username': 'new_username'}
        )
        first_updated = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, {'id': 20})],
        indirect=['motor_api'],
    )
    async def test_update_one_statement_not_none(
            self,
            motor_api: AsyncAPI,
            motor_database,
    ):
        """Test update_one method statement not none."""
        first = await motor_api.get_detail(
            db=motor_database,
        )
        first_username = first['username']
        assert first_username != 'new_username'
        # update first
        await motor_api.update_one(
            db=motor_database,
            update_doc={'username': 'new_username'}
        )
        first_updated = await motor_api.get_detail(
            db=motor_database,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_update_one_document_not_none(
            self,
            motor_api: AsyncAPI,
            motor_database,
    ):
        """Test update_one method document not none."""
        first = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        first_username = first['username']
        assert first_username != 'new_username'

        motor_api.pk_field = None
        # update first
        await motor_api.update_one(
            db=motor_database,
            update_doc={'username': 'new_username'},
            document={'id': 1}
        )

        motor_api.pk_field = 'id'
        first_updated = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_delete(
            self,
            motor_api: AsyncAPI,
            motor_database,
    ):
        """Test delete method."""

        first = await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        )
        assert first['id'] == 1
        await motor_api.delete(motor_database, field_value=1)
        assert await motor_api.get_detail(
            db=motor_database,
            field_value=1,
        ) is None

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_delete_invalid_pk_field(
            self,
            motor_api: AsyncAPI,
            motor_database,
    ):
        """Test delete method invalid pk_field."""
        with pytest.raises(AttributeError):
            await motor_api.delete(motor_database, field_value=1)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', [], None, None, None, None)],
        indirect=['motor_api'],
    )
    async def test_delete_invalid_document(
            self,
            motor_api: AsyncAPI,
            motor_database,
    ):
        """Test delete method invalid document."""
        with pytest.raises(HTTPException):
            await motor_api.delete(motor_database, field_value=1)

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['motor_api'],
    )
    async def test_limit_offset_pagination_first_page(
            self,
            motor_api: AsyncAPI,
            motor_database,
            request_fixture,
    ):
        """Test limit offset pagination first page. Total objects 50."""
        request_fixture.query_params = {}
        response = await motor_api.get_all_with_pagination(motor_database, request_fixture)
        paginate_by = 20
        results = response['results']
        assert results[0]['id'] == 1
        assert results[19]['id'] == 20
        assert response['count'] == paginate_by
        assert response['total'] == NUMBER_OF_OBJECTS
        assert response['page_limit'] == paginate_by
        assert response['total_pages'] == 2
        assert response['previous_page'] is None
        assert response['next_page'] is not None
        assert response['last_page'] is not None

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['motor_api'],
    )
    async def test_limit_offset_pagination_second_page(
            self,
            motor_api: AsyncAPI,
            motor_database,
            request_fixture,
    ):
        """Test limit offset pagination second page. Total objects 50."""
        request_fixture.query_params = {
            'page': 1,
        }
        response = await motor_api.get_all_with_pagination(motor_database, request_fixture)
        results = response['results']
        assert results[0]['id'] == 21
        assert results[19]['id'] == 40
        assert response['count'] == 20
        assert response['previous_page'] is not None
        assert response['next_page'] is not None
        assert response['last_page'] is not None

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['motor_api'],
    )
    async def test_limit_offset_pagination_last_page(
            self,
            motor_api: AsyncAPI,
            motor_database,
            request_fixture,
    ):
        """Test limit offset pagination last page. Total objects 50."""
        request_fixture.query_params = {
            'page': 2,
        }
        response = await motor_api.get_all_with_pagination(motor_database, request_fixture)
        results = response['results']
        assert results[0]['id'] == 41
        assert results[9]['id'] == 50
        assert response['count'] == 10
        assert response['previous_page'] is not None
        assert response['next_page'] is None
        assert response['last_page'] is not None

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, 7, AsyncPaginationCursor,
          {
              'model': 'test_collection',
              'ordering': ['id'],
              'cursor_prefixes': ['next__', 'prev__']
          },
          {'id': {'$gt': 25}},
          )],
        indirect=['motor_api'],
    )
    async def test_cursor_pagination_first_page(
            self,
            motor_api: AsyncAPI,
            motor_database,
            request_fixture,
    ):
        """Test limit offset pagination first page. Total objects 50."""
        request_fixture.query_params = {}
        assert motor_api.pagination_strategy == AsyncPaginationCursor
        response = await motor_api.get_all_with_pagination(motor_database, request_fixture)
        paginate_by = 7
        results = response['results']
        assert results[0]['id'] == 26  # query was id > 25
        assert results[6]['id'] == 32
        assert response['count'] == paginate_by
        assert response['page_limit'] == paginate_by
        assert response['first_page'] is not None
        assert response['previous_page'] is None
        assert response['next_page'] is not None
        assert 'cursor' in response['next_page']

    @pytest.mark.parametrize(
        'motor_api',
        [('test_collection', None, 7, AsyncPaginationCursor,
          {
              'model': 'test_collection',
              'ordering': ['-id'],  # descending
              'cursor_prefixes': ['next__', 'prev__']
          },
          {'id': {'$gt': 25}},
          )],
        indirect=['motor_api'],
    )
    async def test_cursor_pagination_first_page_descending(
            self,
            motor_api: AsyncAPI,
            motor_database,
            request_fixture,
    ):
        """Test limit offset pagination first page descending order. Total objects 50."""
        request_fixture.query_params = {}
        assert motor_api.pagination_strategy == AsyncPaginationCursor
        response = await motor_api.get_all_with_pagination(motor_database, request_fixture)
        paginate_by = 7
        results = response['results']
        assert results[0]['id'] == 50
        assert results[6]['id'] == 44
        assert response['count'] == paginate_by
        assert response['page_limit'] == paginate_by
        assert response['first_page'] is not None
        assert response['previous_page'] is None
        assert response['next_page'] is not None
        assert 'cursor' in response['next_page']
