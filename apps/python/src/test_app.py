import app
import pytest

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_api(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}