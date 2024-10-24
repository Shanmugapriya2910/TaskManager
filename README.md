Here’s the complete `README.md` file with all the instructions for setting up the Task Management API using Django, without including the database configuration details:

```markdown
# Task Management API

This is a simple Task Management API built using Django and Django REST Framework. The API allows basic CRUD (Create, Read, Update, Delete) operations for managing tasks.

## Features

- Create a new task
- Retrieve all tasks or a single task by ID
- Update an existing task
- Delete a task

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Postman (for API testing)

## Installation

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

### 2. Set up a virtual environment

Create a virtual environment for the project using `venv`:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set up Django

Once dependencies are installed, you need to configure Django for the project.

- **Migrate the database** to apply the existing models:

```bash
python manage.py makemigrations
python manage.py migrate
```

- **Run the development server**:

```bash
python manage.py runserver
```

Now, the server will be running at `http://127.0.0.1:8000/`.

## API Endpoints

Below is the list of available API endpoints for managing tasks. Use these endpoints in Postman to perform CRUD operations:

| Method | Endpoint                      | Description                    |
|--------|-------------------------------|--------------------------------|
| POST   | `/api/tasks/create/`           | Create a new task              |
| GET    | `/api/tasks/`                  | Retrieve all tasks             |
| GET    | `/api/tasks/<task_id>/`        | Retrieve a specific task by ID |
| PUT    | `/api/tasks/update/<task_id>/` | Update a task by ID            |
| DELETE | `/api/tasks/delete/<task_id>/` | Delete a task by ID            |

### Sample Payload for POST/PUT

Use the following JSON structure when making `POST` and `PUT` requests:

```json
{
    "title": "Sample Task",
    "description": "This is a sample task.",
    "completed": false
}
```

### Sample API Requests

#### 1. **Create Task** (POST)

- **URL:** `http://127.0.0.1:8000/api/tasks/create/`
- **Method:** `POST`
- **Sample Payload:**
```json
{
    "title": "task",
    "description": "task",
    "completed": false
}
```

#### 2. **Get All Tasks** (GET)

- **URL:** `http://127.0.0.1:8000/api/tasks/`
- **Method:** `GET`
- **Response:**
```json
[
    {
        "id": 1,
        "title": "task",
        "description": "task",
        "completed": false
    }
]
```

#### 3. **Get Task by ID** (GET)

- **URL:** `http://127.0.0.1:8000/api/tasks/1/`
- **Method:** `GET`
- **Response:**
```json
{
    "id": 1,
    "title": "task",
    "description": "task",
    "completed": false
}
```

#### 4. **Update Task** (PUT)

- **URL:** `http://127.0.0.1:8000/api/tasks/update/1/`
- **Method:** `PUT`
- **Sample Payload:**
```json
{
    "title": "task",
    "description": "task",
    "completed": true
}
```

#### 5. **Delete Task** (DELETE)

- **URL:** `http://127.0.0.1:8000/api/tasks/delete/1/`
- **Method:** `DELETE`
- **Response:**
```json
{
    "message": "Task deleted successfully"
}
```





