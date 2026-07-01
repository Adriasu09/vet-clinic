# Vet Clinic API

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-async-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-database-336791)
![License](https://img.shields.io/badge/license-MIT-green)

> A REST API for a veterinary clinic, built with FastAPI and PostgreSQL.

This project manages the core entities of a veterinary clinic — owners, pets, veterinarians, treatments, appointments and medical records — exposing them through a clean, layered REST API. It is a learning project (Factoria F5 bootcamp): the goal is to understand the fundamentals of database connection, ORM modelling, API design, error handling and testing.

## Table of Contents

- [Background](#background)
- [Tech Stack](#tech-stack)
- [Install](#install)
- [Usage](#usage)
- [API](#api)
- [Project Structure](#project-structure)
- [Tests](#tests)
- [Contributing](#contributing)
- [Maintainers](#maintainers)
- [License](#license)

## Background

The API is organised in clear layers, each with a single responsibility:

- **Models** (`app/models/`) — SQLAlchemy 2.0 classes that define the database tables.
- **Schemas** (`app/schemas/`) — Pydantic models that validate what enters and leaves the API.
- **CRUD** (`app/crud/`) — plain functions that talk to the database (queries, inserts, updates).
- **Routers** (`app/routers/`) — FastAPI endpoints grouped by resource.

Cross-cutting concerns are handled in one place: configuration is read once from `.env` (`app/core/config.py`), errors are raised as domain exceptions (`app/exceptions.py`) and translated to HTTP responses by global handlers in `main.py`.

## Tech Stack

- **Python 3.12**
- **FastAPI** — web framework
- **Uvicorn** — ASGI server
- **SQLAlchemy 2.0** — ORM
- **Pydantic / pydantic-settings** — validation and configuration
- **PostgreSQL** (via `psycopg2`) — database, managed with pgAdmin
- **pytest** — testing

## Install

### Prerequisites

- Python 3.12
- PostgreSQL running locally (managed e.g. with pgAdmin)

### Steps (Windows PowerShell)

```powershell
# 1. Clone the repository
git clone <your-repo-url>
cd vet-clinic

# 2. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your environment file from the template and fill in your values
copy .env.example .env
```

> On macOS/Linux use `source .venv/bin/activate` and `cp .env.example .env`.

Then edit `.env` with your PostgreSQL credentials:

```env
APP_NAME=Vet Clinic API
APP_VERSION=1.0.0
APP_DESCRIPTION=Vet Clinic API - Factoria F5

DB_HOST=localhost
DB_PORT=5432
DB_NAME=vet_clinic_db
DB_USER=postgres
DB_PASSWORD=your_password
```

Finally, create the database in pgAdmin (`vet_clinic_db`) and create the tables:

```powershell
python init_db.py
```

## Usage

Run the development server:

```powershell
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`. Open the interactive documentation (Swagger UI) at:

```
http://127.0.0.1:8000/docs
```

From there you can try every endpoint directly in the browser.

## API

All endpoints return JSON. Errors follow standard HTTP semantics (`404` not found, `409` conflict, `422` validation error).

### Owners — `/owners`

| Method | Path            | Description            |
| ------ | --------------- | ---------------------- |
| POST   | `/owners/`      | Create an owner        |
| GET    | `/owners/`      | List all owners        |
| GET    | `/owners/{id}`  | Get an owner by id     |
| PUT    | `/owners/{id}`  | Update an owner        |
| DELETE | `/owners/{id}`  | Delete an owner        |

### Pets — `/pets`

| Method | Path          | Description         |
| ------ | ------------- | ------------------- |
| POST   | `/pets/`      | Create a pet        |
| GET    | `/pets/`      | List all pets       |
| GET    | `/pets/{id}`  | Get a pet by id     |
| PUT    | `/pets/{id}`  | Update a pet        |
| DELETE | `/pets/{id}`  | Delete a pet        |

## Project Structure

```
vet-clinic/
├── app/
│   ├── core/config.py       # Settings loaded from .env
│   ├── crud/                # Database operations
│   ├── models/              # SQLAlchemy models (tables)
│   ├── routers/             # API endpoints
│   ├── schemas/             # Pydantic schemas (validation)
│   ├── database.py          # Engine, session, Base, get_db
│   ├── enums.py             # Domain enums (e.g. appointment status)
│   └── exceptions.py        # Domain exceptions
├── tests/                   # pytest tests
├── init_db.py               # Creates the database tables
├── main.py                  # FastAPI app entry point
├── requirements.txt
└── .env.example
```

## Tests

Tests run against a separate database so they never touch your development data.

```powershell
# 1. Create the test database in pgAdmin: vet_clinic_test_db
# 2. Run the suite
pytest -v
```

## Contributing

This project follows a **GitFlow** branching model:

- `main` — stable releases
- `develop` — integration branch
- `feature/*` — work branches, created from `develop`

Commits follow the [Conventional Commits](https://www.conventionalcommits.org/) style (`feat`, `fix`, `test`, `docs`, `refactor`, `chore`). Open a Pull Request against `develop`.

## Maintainers

[@Adriasu09](https://github.com/Adriasu09) — Adriana Suárez

## License

[MIT](LICENSE) © Adriana Suárez
