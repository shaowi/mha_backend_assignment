import pytest
from flask import json

import app
from globals import USER_ADDED_SUCCESSFULLY

ENDPOINT = "http://localhost:3000/user"


@pytest.fixture
def client():
    with app.app.test_client() as client:
        yield client


def test_get_users_return_correct_users(client):
    response = client.get(ENDPOINT)

    assert response.status_code == 200
    users = json.loads(response.data)
    assert len(users) == 2 and users[0]["name"] == "Alice" and users[1]["name"] == "Bob"


def test_get_user_return_correct_user(client):
    response = client.get(f"{ENDPOINT}/1")
    assert response.status_code == 200
    user = json.loads(response.data)
    assert user["name"] == "Alice"


def test_add_user_return_correct_message(client):
    new_user = {"name": "Charlie", "age": 40}
    response = client.post(
        ENDPOINT, data=json.dumps(new_user), content_type="application/json"
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["message"] == USER_ADDED_SUCCESSFULLY


def test_delete_user_return_correct_message(client):
    response = client.delete(f"{ENDPOINT}/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == USER_ADDED_SUCCESSFULLY
