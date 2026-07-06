# 🏋️ Gymy

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)
![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)
---

# 📖 Project Overview

Gymy is a **Workout Recommendation System** that generates personalized gym workout plans based on a user's profile and preferences.

Users provide information such as:

* Age
* Workout Duration
* Fitness Goal
* Experience Level
* Workout Days Per Week
* Available Equipment
* Injuries or Physical Limitations

Based on these inputs, the application recommends an optimized workout routine using a recommendation engine backed by a MySQL database.

---

# ✨ Features

* Personalized workout recommendations
* FastAPI
* React frontend
* MySQL database
* Dockerized architecture
* Docker Compose support
* Responsive user interface
* Input validation using Pydantic

---

# 🛠 Technology Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* PyMySQL

## Frontend

* React
* Vite
* Axios
* CSS

## Database

* MySQL

## DevOps

* Docker

---

# 🏗 Project Architecture

```text
                    User
                      │
                      ▼
               React Frontend
                      │
              FAST API Requests
                      │
                      ▼
              FastAPI Backend
                      │
            Recommendation Engine
                      │
                      ▼
               MySQL Database
```

---

# 📂 Project Structure

```text
GymRecom/
│
├── Backend/
│   ├── schemas.py
│   ├── engine.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── main.py
│
├── Frontend/
│   ├── src/
│   │     ├── assets/
│   │     ├── components/
│   │     │        ├──F.jsx
│   │     │        └──R.jsx
│   │     ├── App.jsx
│   │     └── main.jsx
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.js
│
├── mysql-init/
│   └── cleaneddataset.sql
│
├── docker-compose.yml
│
└── README.md
```

---

# ⚙️ Installation

## Prerequisites

Install the following software before running the project:

* Docker

---

# Clone the Repository

```bash
git clone https://github.com/AadarshAadi/GymRecom.git

cd GymRecom
```

---

# Run Using Docker (Recommended)

Build and start all containers:

```bash
docker compose up
```

Stop containers:

```bash
docker compose down
```

Remove volumes:

```bash
docker compose down -v
```

---

# Application URLs

Frontend

```
http://localhost:5173
```

Backend

```
http://localhost:8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

ReDoc Documentation

```
http://localhost:8000/redoc
```

---

# Running Without Docker

## Backend

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn main:app --reload
```

---

## Frontend

Install dependencies

```bash
npm install
```

Run development server

```bash
npm run dev
```

---

# Database Setup

The application uses MySQL.

If using Docker, the database is automatically created during startup.

The initialization script creates:

* Database
* Required tables
* Sample exercise data

---

# How the Recommendation Engine Works

1. User enters fitness details.
2. Frontend validates the form.
3. Data is sent to the FastAPI backend.
4. Backend validates the request using Pydantic.
5. Recommendation engine queries the MySQL database.
6. Exercises are filtered based on user preferences.
7. Personalized workout plan is generated.
8. Results are returned as JSON.
9. Frontend displays the recommended workout.

---

# User Inputs

The recommendation engine considers factors such as:

* Age
* Workout Duration
* Experience Level
* Fitness Goal
* Workout Frequency
* Equipment Availability
* Injury Information

These inputs help generate recommendations that are more relevant than generic workout plans.

---

# Validation

The backend validates all incoming requests using Pydantic.

Examples include:

* Missing fields
* Invalid values
* Incorrect data types
* Empty requests

Appropriate HTTP status codes are returned when validation fails.

---

# Docker Containers

The application consists of three independent containers:

## Frontend

* React
* Vite

## Backend

* FastAPI
* Recommendation Engine

## Database

* MySQL

These communicate over a Docker network managed by Docker Compose.

---

# Dataset Source

The Exercise dataset is based on publicly available exercise dataset by 
Niharika Pandit from Kaggle:
* https://www.kaggle.com/datasets/niharika41298/gym-exercise-data?resource=download

---

# Screenshots

![Form Screenshot](Screenshots/1.png)
![Results Screenshot](Screenshots/2.png)
![Results Screenshot](Screenshots/3.png)
---

# Troubleshooting

## Docker won't start

```bash
docker compose down

docker compose up --build
```

---

## Port already in use

Change ports inside:

```
docker-compose.yml
```

or stop the application currently using that port.

---

## Database connection error

Ensure:

* MySQL container is running
* Environment variables are correct
* Docker network is created successfully

---

# Author

**Aadarsh**

GitHub

https://github.com/AadarshAadi

---

# Acknowledgements

Open-source technologies used:

* FastAPI
* React
* Docker
* MySQL
* SQLAlchemy
* Vite
* Axios

