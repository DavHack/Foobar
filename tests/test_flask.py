from foobar import app
from multiprocessing import Process
import pytest
app = app.app

@pytest.fixture
def test_client():
    return app.test_client()


def test_flask(test_client):
    rv = test_client.get('/foo')
    assert rv.status_code == 200
    assert rv.data == b'foo'

def test_bar(test_client):
    rv = test_client.get('/bar')
    assert rv.status_code == 200
    assert rv.data == b'bar'
