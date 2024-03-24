from model.user import User

# Endpoints
USER_ENDPOINT = "/user"
USER_ENDPOINT_WITH_ID = f"{USER_ENDPOINT}/<string:user_id>"

# Messages
ERROR_INVALID_USER_DATA = {"error": "Invalid user data"}
ERROR_USER_NOT_FOUND = {"error": "User not found"}
USER_DELETED_SUCCESSFULLY = {"message": "User deleted successfully"}
USER_ADDED_SUCCESSFULLY = {"message": "User added successfully"}
