# Research Answers

## 1. How HTTP Applications Preserve State

HTTP is inherently stateless, meaning each request is processed independently without memory of previous interactions. To maintain state across multiple requests, web applications use several mechanisms:

**Cookies** are small data fragments stored in the user's browser and sent with each request to the server. They are widely used for managing sessions, storing user preferences, and tracking activity.

**Sessions** involve storing user-specific data on the server. When a user logs in, the server creates a session and provides a session ID (often stored in a cookie) to the client. Future requests include this session ID, enabling the server to retrieve session data and keep the user authenticated.

**Authentication Tokens** such as JWTs (JSON Web Tokens) carry encoded user information and are typically sent in request headers. This approach allows for stateless authentication, as the server does not need to store session data.

For authentication, after a successful login, the server either creates a session or issues a token. The client includes the session ID or token in subsequent requests, allowing the server to recognize the user and maintain their authenticated state throughout their session.

## 2. Django Database Migrations with MariaDB

To run Django database migrations using a server-based relational database like MariaDB, follow these steps:

First, configure Django to use MariaDB by installing a suitable database adapter (such as mysqlclient or mysql-connector-python) via pip. Update the `DATABASES` setting in `settings.py` to specify MariaDB connection details, including the engine (`'django.db.backends.mysql'`), database name, host, port, username, password, and other options.

Migration commands are the same as with SQLite: use `python manage.py makemigrations` to generate migration files from model changes, and `python manage.py migrate` to apply those changes to the database. Django will produce SQL statements compatible with MySQL/MariaDB.

For production environments, take extra precautions: always back up your database before migrating, test migrations in a staging environment, and consider strategies for zero-downtime migrations with large datasets. Use the `--plan` option to preview migration steps, and `migrate --fake` for complex scenarios. Ensure security by assigning appropriate database user permissions, using SSL for remote connections, and storing sensitive credentials in environment variables rather than hardcoding them.