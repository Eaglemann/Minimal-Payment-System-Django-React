# Minimal Payment System - Django & React

This project is a full-stack CRUD application built using React/Typescript (Next.js) for the frontend and Django for the backend. It is designed to manage issues.

## Project Goal

The primary goal of this application is to provide a streamlined system for creating, reading, updating, and deleting issues. It serves as a foundation for more complex issue tracking or project management systems, demonstrating best practices in full-stack development with React and Django.

## Technologies Used

*   **Frontend:** React, Typescript, Next.js
*   **Backend:** Django
*   **Database:** (Implicitly using Django's default SQLite or configured database)

## Backend Setup (Django)

### Getting started (Docker)

```bash
$ docker-compose build backend
$ docker-compose run backend ./manage.py migrate
$ docker-compose run --service-ports backend ./manage.py runserver 0.0.0.0:8000
```

### Getting started (Without Docker)

> **- Requires Python 3.9+ -**

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver 8000
```

### Creating a superuser (Django Admin Access)

```bash
$ ./manage.py createsuperuser
```

Access the Django admin interface at http://localhost:8000/admin/

### Running Backend Tests

```bash
$ ./manage.py test
```

## Frontend Setup (React/Next.js)

### Getting started (Docker)

```bash
$ docker-compose build frontend
$ docker-compose run --service-ports frontend npm run dev
```

### Getting started (Without Docker)

> **- Requires Node.js 14+ -**

```bash
$ npm install
$ npm run dev
```

The frontend will be accessible at http://localhost:3000.

### Running Frontend Tests

```bash
$ npm test
```

## API Endpoints

This section documents the API endpoints for managing issues and users. All endpoints return JSON responses.

### Issues API

#### `GET /api/issues` (app/api/issues/route.ts)

*   **Description:** Retrieves a list of all issues.
*   **Authentication:** Required
*   **Request Method:** GET
*   **Parameters:** None
*   **Request Example:**

    ```
    GET /api/issues
    ```
*   **Response Example:**

    ```json
    [
      {
        "id": 1,
        "title": "Issue 1",
        "description": "Description of issue 1",
        "status": "open"
      },
      {
        "id": 2,
        "title": "Issue 2",
        "description": "Description of issue 2",
        "status": "closed"
      }
    ]
    ```

#### `POST /api/issues` (app/api/issues/route.ts)

*   **Description:** Creates a new issue.
*   **Authentication:** Required
*   **Request Method:** POST
*   **Parameters:** `title` (string, required), `description` (string, required), `status` (string, optional, defaults to "open")
*   **Request Example:**

    ```json
    POST /api/issues
    Content-Type: application/json

    {
      "title": "New Issue",
      "description": "Details of the new issue"
    }
    ```

*   **Response Example:**

    ```json
    {
      "id": 3,
      "title": "New Issue",
      "description": "Details of the new issue",
      "status": "open"
    }
    ```

#### `GET /api/issues/:id` (app/api/issues/[id]/route.ts)

*   **Description:** Retrieves a specific issue by ID.
*   **Authentication:** Required
*   **Request Method:** GET
*   **Parameters:** `id` (integer, required)
*   **Request Example:**

    ```
    GET /api/issues/1
    ```

*   **Response Example:**

*   **Description:** Updates an existing issue.
*   **Authentication:** Required
*   **Request Method:** PUT
*   **Parameters:** `id` (integer, required), `title` (string, optional), `description` (string, optional), `status` (string, optional)
*   **Request Example:**

json
    PUT /api/issues/1
    Content-Type: application/json

    {
      "title": "Updated Issue Title",
      "status": "closed"
    }
    
    DELETE /api/issues/1
    
    GET /api/users
    Authentication is handled using NextAuth.js via `app/api/auth/[...nextAuth]/route.ts`.  This endpoint provides authentication routes for various providers (e.g., Google, GitHub, email/password).

#### Authentication Flow

1.  The user initiates the login process through the frontend.
2.  The frontend redirects the user to the appropriate NextAuth.js route (e.g., `/api/auth/signin`).
3.  NextAuth.js handles the authentication with the chosen provider.
4.  Upon successful authentication, NextAuth.js creates a session and redirects the user back to the application.

#### Setup

> Configure your NextAuth.js providers in `app/api/auth/[...nextAuth]/route.ts`.  You'll need to set up the necessary credentials and environment variables for each provider you intend to use.  Refer to the NextAuth.js documentation for detailed instructions: [https://next-auth.js.org/configuration/providers](https://next-auth.js.org/configuration/providers)

## Contribution Guidelines

We welcome contributions to this project!  Please follow these guidelines:

1.  **Coding Style:**  Adhere to the existing coding style.  Use consistent indentation and naming conventions.
2.  **Testing:**  Write unit tests for any new features or bug fixes. Ensure that all tests pass before submitting a pull request.
3.  **Pull Requests:**
    *   Create a new branch for your changes.
    *   Submit pull requests to the `main` branch.
    *   Include a clear and concise description of your changes in the pull request.
    *   Address any feedback from reviewers.

## Deployment

> The application can be deployed using various platforms like Vercel, Netlify, or AWS. For deploying the Django backend, you might consider using platforms like Heroku, PythonAnywhere, or a cloud provider like AWS, Google Cloud, or Azure. Ensure you configure environment variables properly for production.

A basic deployment process might involve:

1.  Building the Next.js frontend: `npm run build`
2.  Configuring a WSGI server (e.g., Gunicorn) for the Django backend.
3.  Setting up a database (e.g., PostgreSQL) and configuring Django to use it.
4.  Deploying the frontend and backend to your chosen platform.

## Layout and Styling

*   `app/layout.tsx`: This file defines the root layout of the application. It typically includes the basic HTML structure, global styles, and any components that should be present on all pages (e.g., navigation bar, footer).
*   `app/page.tsx`: This file represents the main page of the application (the homepage).  It contains the content specific to the homepage.

> Modify `app/layout.tsx` to change the overall structure and styling of your application.  Modify `app/page.tsx` to change the content of the homepage.

