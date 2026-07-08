# Installation Guide

This guide explains how to install and run the GYMY application.

---

# Prerequisites

Before getting started, ensure the following software is installed on your system:

- Git
- Docker Desktop (includes Docker Compose)

Verify your installation:

```bash
docker --version
docker compose version
```

---

# Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/AadarshAadi/GymRecom.git

cd GymRecom
```

---

# Running with Docker (Recommended)

Docker Compose automatically starts all required services:

- Frontend (React + Vite)
- Backend (FastAPI)
- MySQL Database

### Build and start the application

```bash
docker compose up
```

### Rebuild after making changes

```bash
docker compose up --build
```

### Run in detached mode

```bash
docker compose up -d
```

### Stop the application

```bash
docker compose down
```

### Remove containers and volumes

```bash
docker compose down -v
```

---

# Application URLs

Once the containers are running, the application can be accessed at:

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Backend API | http://localhost:8000 |
| Swagger Documentation | http://localhost:8000/docs |
| ReDoc Documentation | http://localhost:8000/redoc |

---

# Running Without Docker

## Backend

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the FastAPI server

```bash
uvicorn main:app --reload
```

---

## Frontend

### Install dependencies

```bash
npm install
```

### Start the development server

```bash
npm run dev
```

---

# Database Setup

The application uses a MySQL database.

When running with Docker Compose:

- A MySQL container is created automatically.
- The database is initialized on startup.
- The SQL dataset is imported automatically.
- The backend connects to the database without additional configuration.

No manual database setup is required when using Docker.

---

# Troubleshooting

## Docker fails to start

Rebuild the containers:

```bash
docker compose down

docker compose up --build
```

---

## Port already in use

If one of the required ports is occupied:

- Edit the port mappings in `docker-compose.yml`.
- Restart the application after saving the changes.

---

## Database connection error

Check that:

- The MySQL container is running.
- Docker Compose created the network successfully.
- Database credentials are configured correctly.
- The backend starts after the database initialization completes.