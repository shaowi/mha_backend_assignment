# Backend Flask API

This is a Flask application that provides a RESTful API for managing users

## Set up

1. Clone the repository

```bash
git clone https://github.com/shaowi/mha_backend_assignment.git
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python3 app.py
```

The application will start on localhost port `3000`

### API Endpoints

The application provides the following endpoints:

- `GET /user/<user_id>`: Get a user by ID.
- `GET /user`: Get all users.
- `POST /user`: Add a new user.
- `DELETE /user/<user_id>`: Delete a user by ID.

The user object has the following fields:

- `id`: The user ID.
- `name`: The user name.
- `age`: The user age.

### Testing

To run the tests, run the following command from the root directory:

```bash
pytest
```

### Logging

The application logs are written to backend.log

### Notes on Deployment

- This application can be deployed on several platforms, including Heroku, AWS, and Google Cloud.
- Containerization with Docker is also an option and can be used to deploy the application on Kubernetes.
- Sensitive data should be stored in environment variables and not in the codebase during deployment.
- The application should also be secured with HTTPS.
- Setting up a CI/CD pipeline is also recommended to automate the deployment process.
- Use monitoring tools to monitor the application's performance and health.
- Use a load balancer to distribute traffic across multiple instances of the application for scalability.
- Ensure that the application is secure and follows best practices for security.
