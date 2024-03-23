import handler
from model.user import User

sample_users = [
    User(id="1", name="Alice", age=30),
    User(id="2", name="Bob", age=35),
]


def test_get_user_by_id_has_user_returns_correct_user():
    user = handler.get_user_by_id("1", sample_users)
    assert user.name == "Alice" and user.age == 30


def test_get_user_by_id_no_user_returns_none():
    user = handler.get_user_by_id("3", sample_users)
    assert user is None


def test_handle_get_user_no_user_returns_correct_message():
    message, code = handler.handle_get_user("3", sample_users)
    assert message == handler.ERROR_USER_NOT_FOUND and code == 404


def test_handle_add_user_valid_fields_returns_success_message():
    data = {"name": "Charlie", "age": 40}
    message, code = handler.handle_add_user(data, sample_users)
    assert message == handler.USER_ADDED_SUCCESSFULLY and code == 201


def test_handle_delete_user_no_user_returns_error_message():
    message, code = handler.handle_delete_user("3", sample_users)
    assert message == handler.ERROR_USER_NOT_FOUND and code == 404
