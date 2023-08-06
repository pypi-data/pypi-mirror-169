import pytest
from fastapi.exceptions import HTTPException

from fastapi_views.ext.pymongo.pagination.core import PaginationCursor
from fastapi_views.ext.pymongo.sync_api import SyncAPI

NUMBER_OF_OBJECTS = 50  # number of objects created by sync db


@pytest.fixture
def pymongo_api(request):
    collection, pk_field, paginate_by, strategy, kwargs, statement = request.param
    return SyncAPI(
        model=collection,
        pk_field=pk_field,
        paginate_by=paginate_by,
        pagination_strategy=strategy,
        pagination_kwargs=kwargs,
        statement=statement,
    )


class TestSyncAPI:
    """Test pymongo api cls."""

    @pytest.mark.parametrize('test_input', [None, ''])
    def test_init_model_raise_value_error(self, test_input):
        """Test collection value error."""
        with pytest.raises(ValueError):
            assert SyncAPI(model=test_input)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_session_get_all_raises(self, pymongo_api: SyncAPI):
        """Test session attr in get_all method."""
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session=False)
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session=True)
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session='foo_str')

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_session_get_detail_raises(self, pymongo_api: SyncAPI):
        """Test session attr in get_detail method."""
        with pytest.raises(TypeError):
            pymongo_api.get_detail(db=None, session=False)
        with pytest.raises(TypeError):
            pymongo_api.get_detail(db=None, session=True)
        with pytest.raises(TypeError):
            pymongo_api.get_detail(db=None, session='foo_str')

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_session_update_one_raises(self, pymongo_api: SyncAPI):
        """Test session attr in update_one method."""
        with pytest.raises(TypeError):
            pymongo_api.update_one(db=None, session=False)
        with pytest.raises(TypeError):
            pymongo_api.update_one(db=None, session=True)
        with pytest.raises(TypeError):
            pymongo_api.update_one(db=None, session='foo_str', update_doc={})

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_session_create_raises(self, pymongo_api: SyncAPI):
        """Test session attr in create method."""
        with pytest.raises(TypeError):
            pymongo_api.create(db=None, session=False, document={})
        with pytest.raises(TypeError):
            pymongo_api.create(db=None, session=True, document={})
        with pytest.raises(TypeError):
            pymongo_api.create(db=None, session='foo_str', document={})

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_session_delete_raises(self, pymongo_api: SyncAPI):
        """Test session attr in delete method."""
        with pytest.raises(TypeError):
            pymongo_api.delete(db=None, session=False, field_value=None)
        with pytest.raises(TypeError):
            pymongo_api.delete(db=None, session=True, field_value=None)
        with pytest.raises(TypeError):
            pymongo_api.delete(db=None, session='foo_str', field_value=None)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_get_all_statement_raises(self, pymongo_api: SyncAPI):
        """Test statement attr in get_all method."""
        with pytest.raises(TypeError):
            class Cls:
                pass

            pymongo_api.get_all(db=None, session=Cls)
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session=False)
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session=True)
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session='foo_str')
        with pytest.raises(TypeError):
            pymongo_api.get_all(db=None, session=2)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, {})],
        indirect=['pymongo_api'],
    )
    def test_session_get_methods(self, pymongo_api: SyncAPI, pymongo_database, client_session):
        """Test session correct type. In some cases session is not implemented in mongomock yet."""
        assert pymongo_api.get_all(db=pymongo_database, session=client_session)
        assert pymongo_api.get_detail(db=pymongo_database, session=client_session)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, {})],
        indirect=['pymongo_api'],
    )
    def test_get_all(self, pymongo_api: SyncAPI, pymongo_database, client_session):
        """Test get_all method."""
        response = pymongo_api.get_all(db=pymongo_database, session=client_session)
        assert len(list(response)) == NUMBER_OF_OBJECTS
        response = pymongo_api.get_all(db=pymongo_database, session=client_session, limit=10)
        assert len(list(response)) == 10
        response = pymongo_api.get_all(
            db=pymongo_database,
            session=client_session,
            limit=5,
            skip=5,
        )
        response_list = list(response)
        assert response_list[0]['id'] == 6  # first 5 result skipped
        assert len(response_list) == 5  # limit value

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_get_detail(self, pymongo_api: SyncAPI, pymongo_database):
        """Test get_detail method with id as pk_field."""
        response = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        assert response['id'] == 1

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_get_detail_pk_field(self, pymongo_api: SyncAPI, pymongo_database):
        """Test get_detail method with None as pk_field."""
        with pytest.raises(AttributeError):
            pymongo_api.get_detail(
                db=pymongo_database,
                field_value=1,
            )

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, {'id': 15})],
        indirect=['pymongo_api'],
    )
    def test_get_detail_statement(self, pymongo_api: SyncAPI, pymongo_database):
        """Test get_detail method with None as pk_field and custom statement."""
        response = pymongo_api.get_detail(
            db=pymongo_database,
        )
        assert response['id'] == 15

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_get_detail_not_found(self, pymongo_api: SyncAPI, pymongo_database):
        """Test get_detail method not found."""
        with pytest.raises(HTTPException):
            pymongo_api.get_detail(
                db=pymongo_database,
                field_value=51,
            )

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_create(self, pymongo_api: SyncAPI, pymongo_database):
        """Test create method."""
        new_doc = {'username': 'john', 'age': 22, 'id': 111}
        pymongo_api.create(
            db=pymongo_database,
            document=new_doc,
        )
        latest = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=new_doc['id'],
        )
        assert latest['username'] == 'john'
        assert latest['age'] == 22

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_create_invalid_document(self, pymongo_api: SyncAPI, pymongo_database):
        """Test create method invalid document."""
        new_doc = False
        with pytest.raises(TypeError):
            pymongo_api.create(
                db=pymongo_database,
                document=new_doc,
            )

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_update_one_doc_none(self, pymongo_api: SyncAPI, pymongo_database):
        """Test update_one method document none."""
        first = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        first_username = first['username']
        assert first_username != 'new_username'
        # update first
        pymongo_api.update_one(
            db=pymongo_database,
            field_value=1,
            update_doc={'username': 'new_username'}
        )
        first_updated = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, {'id': 20})],
        indirect=['pymongo_api'],
    )
    def test_update_one_statement_not_none(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
    ):
        """Test update_one method statement not none."""
        first = pymongo_api.get_detail(
            db=pymongo_database,
        )
        first_username = first['username']
        assert first_username != 'new_username'
        # update first
        pymongo_api.update_one(
            db=pymongo_database,
            update_doc={'username': 'new_username'}
        )
        first_updated = pymongo_api.get_detail(
            db=pymongo_database,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_update_one_document_not_none(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
    ):
        """Test update_one method document not none."""
        first = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        first_username = first['username']
        assert first_username != 'new_username'

        pymongo_api.pk_field = None
        # update first
        pymongo_api.update_one(
            db=pymongo_database,
            update_doc={'username': 'new_username'},
            document={'id': 1}
        )

        pymongo_api.pk_field = 'id'
        first_updated = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        assert first_updated['username'] != first_username
        assert first_updated['username'] == 'new_username'

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', 'id', None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_delete(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
    ):
        """Test delete method."""

        first = pymongo_api.get_detail(
            db=pymongo_database,
            field_value=1,
        )
        assert first['id'] == 1
        pymongo_api.delete(pymongo_database, field_value=1)
        with pytest.raises(HTTPException):  # deleted
            pymongo_api.get_detail(
                db=pymongo_database,
                field_value=1,
            )

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_delete_invalid_pk_field(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
    ):
        """Test delete method invalid pk_field."""
        with pytest.raises(AttributeError):
            pymongo_api.delete(pymongo_database, field_value=1)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', [], None, None, None, None)],
        indirect=['pymongo_api'],
    )
    def test_delete_invalid_document(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
    ):
        """Test delete method invalid document."""
        with pytest.raises(HTTPException):
            pymongo_api.delete(pymongo_database, field_value=1)

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['pymongo_api'],
    )
    def test_limit_offset_pagination_first_page(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
            request_fixture,
    ):
        """Test limit offset pagination first page. Total objects 50."""
        request_fixture.query_params = {}
        response = pymongo_api.get_all_with_pagination(pymongo_database, request_fixture)
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
        'pymongo_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['pymongo_api'],
    )
    def test_limit_offset_pagination_second_page(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
            request_fixture,
    ):
        """Test limit offset pagination second page. Total objects 50."""
        request_fixture.query_params = {
            'page': 1,
        }
        response = pymongo_api.get_all_with_pagination(pymongo_database, request_fixture)
        results = response['results']
        assert results[0]['id'] == 21
        assert results[19]['id'] == 40
        assert response['count'] == 20
        assert response['previous_page'] is not None
        assert response['next_page'] is not None
        assert response['last_page'] is not None

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, 20, None, {}, {})],
        indirect=['pymongo_api'],
    )
    def test_limit_offset_pagination_last_page(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
            request_fixture,
    ):
        """Test limit offset pagination last page. Total objects 50."""
        request_fixture.query_params = {
            'page': 2,
        }
        response = pymongo_api.get_all_with_pagination(pymongo_database, request_fixture)
        results = response['results']
        assert results[0]['id'] == 41
        assert results[9]['id'] == 50
        assert response['count'] == 10
        assert response['previous_page'] is not None
        assert response['next_page'] is None
        assert response['last_page'] is not None

    @pytest.mark.parametrize(
        'pymongo_api',
        [('test_collection', None, 7, PaginationCursor,
          {
              'model': 'test_collection',
              'ordering': ['id'],
              'cursor_prefixes': ['next__', 'prev__']
          },
          {'id': {'$gt': 25}},
          )],
        indirect=['pymongo_api'],
    )
    def test_cursor_pagination_first_page(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
            request_fixture,
    ):
        """Test limit offset pagination first page. Total objects 50."""
        request_fixture.query_params = {}
        assert pymongo_api.pagination_strategy == PaginationCursor
        response = pymongo_api.get_all_with_pagination(pymongo_database, request_fixture)
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
        'pymongo_api',
        [('test_collection', None, 7, PaginationCursor,
          {
              'model': 'test_collection',
              'ordering': ['-id'],  # descending
              'cursor_prefixes': ['next__', 'prev__']
          },
          {'id': {'$gt': 25}},
          )],
        indirect=['pymongo_api'],
    )
    def test_cursor_pagination_first_page_descending(
            self,
            pymongo_api: SyncAPI,
            pymongo_database,
            request_fixture,
    ):
        """Test limit offset pagination first page descending order. Total objects 50."""
        request_fixture.query_params = {}
        assert pymongo_api.pagination_strategy == PaginationCursor
        response = pymongo_api.get_all_with_pagination(pymongo_database, request_fixture)
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
