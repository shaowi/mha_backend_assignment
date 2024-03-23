import logging
from flask import Flask, request

from globals import USER_ENDPOINT, USER_ENDPOINT_WITH_ID
from handler import (
    handle_add_user,
    handle_delete_user,
    handle_get_all_users,
    handle_get_user,
)
from model.user import User

app = Flask(__name__)
users = [
    User(id="1", name="Alice", age=30),
    User(id="2", name="Bob", age=35),
]

# Logging configuration
logging.basicConfig(filename="backend.log", level=logging.INFO, filemode="w")


# Endpoint to get user by ID
@app.route(USER_ENDPOINT_WITH_ID, methods=["GET"])
def get_user(user_id):
    return handle_get_user(user_id, users)


# Endpoint to get user by ID
@app.route(USER_ENDPOINT, methods=["GET"])
def get_users():
    return handle_get_all_users(users)


# Endpoint to add a new user
@app.route(USER_ENDPOINT, methods=["POST"])
def add_user():
    data = request.json
    return handle_add_user(data, users)


# Endpoint to delete an user by ID
@app.route(USER_ENDPOINT_WITH_ID, methods=["DELETE"])
def delete_user(user_id):
    return handle_delete_user(user_id, users)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
