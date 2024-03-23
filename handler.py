import logging
import uuid

from flask import jsonify
from globals import (
    ERROR_USER_NOT_FOUND,
    USER_ADDED_SUCCESSFULLY,
    USER_DELETED_SUCCESSFULLY,
)
from model.user import User


def get_user_by_id(user_id, users: list[User]):
    for user in users:
        if user.id == user_id:
            return user
    return None


def handle_get_all_users(users):
    return jsonify([user.to_dict() for user in users])


def handle_get_user(user_id, users):
    user = get_user_by_id(user_id, users)
    if user:
        return jsonify(user), 200
    else:
        return ERROR_USER_NOT_FOUND, 404


def handle_add_user(data, users: list[User]):
    required_fields = ["name", "age"]
    missing_required_fields = [field for field in required_fields if field not in data]
    if missing_required_fields:
        return (
            jsonify(
                {
                    "error": "Missing required fields",
                    "missing_fields": missing_required_fields,
                }
            ),
            400,
        )

    data["id"] = str(uuid.uuid4())
    user: User = User.from_dict(data)
    users.append(user)
    logging.info(f"Added user: {data}\n")
    logging.info(f"Current users: {','.join([user.name for user in users])}\n")
    return USER_ADDED_SUCCESSFULLY, 201


def handle_delete_user(user_id, users: list[User]):
    user = get_user_by_id(user_id, users)
    if user:
        users.remove(user)
        logging.info(f"Deleted user: {user}\n")
        logging.info(f"Current users: {','.join([user.name for user in users])}\n")
        return USER_DELETED_SUCCESSFULLY, 200
    else:
        return ERROR_USER_NOT_FOUND, 404
