# Python Flask SQLite App Docker Container

This Docker container sets up a Python Flask application with SQLite as the database. It provides a basic web application for managing user names.

## Requirements

- Docker
- Docker Compose

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd python-flask-sqlite-app
   ```

2. Build and run the Docker container using Docker Compose:

   ```bash
   docker-compose up -d
   ```

3. Access the application:

   Open a web browser and navigate to `http://localhost:5000` to access the Flask application.

## Notes

- The Docker Compose configuration uses version 3.7.
- The Python Flask application is built on top of the Python 3.9 Docker image.
- The SQLite database file is stored in the `src` directory as `database.db`.
- The Flask application code is located in the `src` directory.
- The `requirements.txt` file specifies the required Python packages and their versions:
  - Flask==2.3.2
  - Gunicorn==20.1.0
- The application uses Gunicorn as the HTTP server to run the Flask application.
- The Docker container exposes port 5000, which is mapped to port 5000 on the host machine.
- The `index.html` template is used to render a demo home page, where users can submit their names and view the list of users.
- The application automatically creates a "users" table in the SQLite database if it doesn't exist.
- The Docker container performs a health check every 30 seconds to ensure the Flask application is accessible.

## Additional Considerations

- Consider using a named volume instead of a bind mount for the SQLite database file to ensure data persistence and better manageability.
- Separate the database initialization code from the application code and consider using database migration tools.
- Handle security concerns, such as sanitizing user input, protecting against SQL injection, and securing the application and database connections.
- Depending on your deployment environment and scale requirements, consider using a production-ready web server like Nginx in front of Gunicorn.
- Implement appropriate backup and recovery strategies for the SQLite database file.
