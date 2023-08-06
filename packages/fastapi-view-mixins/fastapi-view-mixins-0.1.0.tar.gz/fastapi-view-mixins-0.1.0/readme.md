## What is it?
Package that contains mixins with built-in limit offset and cursor pagination. Destined to build an
API. Easy to use.

Integrated with
1. SqlAlchemy
2. Pymongo
3. Motor - asyncio

### List of available mixins:

1. APIListMixin
2. APIDetailMixin
3. APIUpdateMixin
4. APICreateMixin
5. APIDestroyMixin

### List of available pagination strategies:

1. PaginationLimitOffset / AsyncPaginationLimitOffset - default
2. PaginationCursor / AsyncPaginationCursor

### Built on:

1. fastapi==0.79.0
2. pytest==7.1.2
3. pytest-asyncio==0.19.0
4. SQLAlchemy==1.4.39
5. aiosqlite==0.17.0 # testing purpose
6. pymongo==4.2.0
7. motor==3.0.0
8. mongomock==4.1.2 # testing purpose
9. mongomock-motor==0.0.12 # testing purpose


### Base usage:

#### Motor List view:

```python
# views.py
from fastapi_views.ext.motor.mixins import APIListMixin 


class FooListView(APIListMixin):
    model = 'foo'  # collection name


# urls.py
from fastapi import (APIRouter, Depends)

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/all', response_model=list[SomePydanticModel])
async def get_foo(
        db: AsyncIOMotorDatabase = Depends(get_motor_db),  # required
):
    documents = []
    cur = FooListView().get_all(db)  # cursor is returned, default limit 100, skip 0
    async for document in cur:
        document.pop('_id')  # if you want to return _id you have to work around it by yourself
        documents.append(document)
    return documents
```

You can also override mixin attrs to make it a bit shorter

```python
# urls.py
from fastapi import (APIRouter, Depends)
from fastapi_views import utils
from fastapi_views.views.mixins import BaseAPIListMixin

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/all', response_model=list[SomePydanticModel])
async def get_foo(
        db: AsyncIOMotorDatabase = Depends(get_motor_db)
):
    cur = FooListView(attrs={'model': 'foo'}).get_all(db)
    ...
```


#### Motor list view using pagination:

```python
# views.py
from fastapi_views.ext.motor.mixins import APIListMixin 


class FooListView(APIListMixin):
    model = 'foo'
    paginate_by = 15


# urls.py
from fastapi import (APIRouter, Depends)
from fastapi_views.pagination.schema import LimitOffsetPage

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/all', response_model=LimitOffsetPage.include(SomePydanticModel))
async def get_foo(request: Request, db: Database = Depends(get_motor_db)):
    return await FooListView().get_all_with_pagination(db, request)

result_schema_example = {
  "count": 0,
  "total": 0,
  "total_pages": 0,
  "page_limit": 0,
  "next_page": "string",
  "previous_page": "string",
  "last_page": "string",
  "results": [
    {
      "name": "string",
      "age": 0
    }
  ]
}
```

#### List view cursor pagination example:

```python
# views.py
from fastapi_views.ext.motor.mixins import APIListMixin
from fastapi_views.ext.motor.pagination.core import AsyncPaginationCursor
from sqlalchemy import select, and_
from sqlalchemy.orm import joinedload, Load
from sqlalchemy.sql import Select


class FooListView(APIListMixin):
    model = 'foo'
    paginate_by = 10
    pagination_strategy = AsyncPaginationCursor
    
    # Motor example
    def get_statement(self):
        """As default returns {}."""
        return {'name': 'John', 'age': {'$gt': 20}}

    def get_pagination_kwargs(self):
        """
        As default returns {
            'model': self.model,
            'ordering': ['id'],
            'cursor_prefixes': ['next__', 'prev__']
        }
        """
        kw = super().get_pagination_kwargs()
        kw['ordering'] = ['-created']
        return kw

    # SQLAlchemy example
    def get_statement(self) -> Select:
        """As default returns select(self.model)."""

        statement = select(self.model).options(
            Load(self.model).load_only(self.model.title, self.model.published),
        ).options(
            joinedload(self.model.fk_related, innerjoin=True).
            load_only(Fk_related_model.username, Fk_related_model.email)
        ).where(and_(self.model.id > 0, self.model.id < 100))

        return statement

# urls.py
from fastapi import (APIRouter, Depends)
from fastapi_views.pagination.schema import CursorPage

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/all', response_model=CursorPage.include(SomePydanticModel))
async def get_foo(request: Request, db: Database = Depends(get_motor_db)):
    return await FooListView().get_all_with_pagination(db, request)

result_schema_example = {
  "count": 0,
  "page_limit": 0,
  "first_page": "string",
  "next_page": "string",
  "previous_page": "string",
  "results": [
    {
      "name": "string",
      "age": 0
    }
  ]
}
```
#### Detail/Update/Delete view:

Default ***field_name*** for detail/update/delete view is set to ***id / _id***. To override do as below

```python
# views.py
class FooDetailUpdateDeleteView(RealtedMixin):
    ...
    pk_field = 'field_name'
```

### Some examples of sqlAlchemy usage

#### List view:

```python
# views.py
from fastapi_views.ext.sql_alchemy.mixins import APIListMixin


class FooListView(APIListMixin):
    model = Foo


# urls.py
from fastapi import (APIRouter, Depends)
from fastapi_views import utils

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/all', response_model=list[SomePydanticModel])
async def get_foo(
        session: Session = Depends(db_session),
):
    return utils.scalars(FooListView().get_all(session=session, limit=50))
```

#### Detail view:

```python
# views.py
from fastapi_views.ext.sql_alchemy.mixins import APIDetailMixin


class FooDetailView(APIDetailMixin):
    model = Foo
    
    def get_statement(self) -> Select:
        statement = select(Foo).options(
            Load(Foo).load_only(Foo.title, Foo.published),
        ).options(
            joinedload(Foo.user, innerjoin=True).
            load_only(FooFK.username, FooFK.email)
        ).where(getattr(Foo, self.pk_field) == self.kwargs['pk'])
    
        return statement

    def get_detail(self, *args, **kwargs):
        return super().get_detail(session=self.kwargs['db'])


# urls.py
from fastapi import (APIRouter, Depends)

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/{pk}')
async def get_foo(pk: int, db = Depends(db_session.get_session)):
    return FooDetailView(pk=pk, db=db).get_detail()
```

#### Update view:

```python
# views.py
from fastapi_views.ext.sql_alchemy.mixins import APIUpdateMixin


class FooUpdateView(APIUpdateMixin):
    model = Foo


# urls.py
from fastapi import (APIRouter, Depends)

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/{pk}')
async def get_foo(pk: int, session: Session = Depends(db_session)):
    return FooUpdateView().update_one(field_value=pk, session=session, data={})
```

#### Delete view:

```python
# views.py
from fastapi_views.ext.sql_alchemy.mixins import APIDestroyMixin


class FooDeleteView(APIDestroyMixin):
    model = Foo


# urls.py
from fastapi import (APIRouter, Depends)

foo_router = APIRouter(
    prefix='/foo',
    tags=['Foo']
)


@foo_router.get('/{slug}')
async def get_foo(slug: str, session: Session = Depends(db_session)):
    return FooDeleteView().delete(session=session, field_value=slug)
```

Download on https://pypi.org/project/fastapi-view-mixins/