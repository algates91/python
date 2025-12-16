from main import app
from fastapi.testclient import TestClient

test_client = TestClient(app=app)


def test_root_endpoint():
    '''
    Test for validating the root endpoint
    '''
    response = test_client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()['message']


def test_user_endpoint():
    '''
    Docstring for test_user_endpoint
    '''
    response = test_client.get("/user")
    assert response.status_code == 200
    assert "running" in response.json()['message']


def test_user_endpoint_without_auth():
    '''
    Docstring for test_user_endpoint
    '''
    response = test_client.get("/user/allusers")
    assert response.status_code == 401

def test_user_endpoint_with_auth():
    '''
    Docstring for test_user_endpoint
    '''
    response = test_client.get("/user/allusers")
    assert response.status_code == 401