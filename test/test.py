import pytest
from fastapi.testclient import TestClient
from main import app
from auth import create_jwt_token

from httpx import AsyncClient, ASGITransport

client = TestClient(app=app)

token_data = { "name":"test user","role":"robotic ID"}
jwt = create_jwt_token(token_data)
header={"Authorization": f"Bearer {jwt}"}

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_tasks_without_auth():
    response = client.get("/tasks")
    assert response.status_code == 401

def test_task_with_auth():
    response = client.get("/tasks", headers=header)
    assert response.status_code == 200

def test_post_task():
    input={"title":"test task"}
    response = client.post("/tasks", headers=header, json=input)
    assert response.status_code==200

@pytest.mark.asyncio
async def test_async_getTask():
    async with AsyncClient( transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/tasks")
    assert response.status_code==401


