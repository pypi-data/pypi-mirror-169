from unittest.mock import MagicMock

import pytest
from fastapi.requests import Request


class MockRequest:
    """Request cls required to test pagination."""

    class State:
        def __init__(self):
            self.paginate_by = None

    def __init__(self):
        self.state = self.State()
        self.query_params = None
        self.url = None


@pytest.fixture()
def request_fixture():
    mock = MagicMock(spec=Request, return_value=MockRequest())
    mock.url = 'https://example.com'
    return mock
