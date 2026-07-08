# 🏋️ GYMY

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green.svg)
![React](https://img.shields.io/badge/React-Frontend-61DAFB.svg)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg)

---

# 📖 Project Overview

GYMY is a **Workout Routine Recommendation System** that generates personalized gym workout plans based on a user's profile and preferences.

Users provide information such as:

- Age
- Workout Duration
- Fitness Goal
- Experience Level
- Workout Days Per Week
- Available Equipment
- Injuries or Physical Limitations

Based on these inputs, the application recommends optimized workout routines using a recommendation engine backed by a MySQL database.

The project demonstrates the use of modern full-stack development technologies by combining a React frontend, FastAPI backend, MySQL database, and Docker containerization into a scalable recommendation system.

---

# 🎯 Why I Chose This Project

I chose to develop a **Workout Routine Recommendation System** because I have faced similar issue while starting my fitness journey in past.

Most people going to the gym have no clue about what exercises they need to do, how long or how many sets and reps they need to do. This application is a nice gateway to explore gym plans based on one's personal restrictions such as durations and days of week.

This project allowed me to build a practical recommendation system while applying concepts from full-stack development, database management and Docker containerization. It also provided an opportunity to integrate multiple technologies into a complete production-like application.

---

# ⭐ What Makes This Project Special

Unlike traditional workout applications that display the same exercises for every user, GYMY generates personalized workout routine recommendations based on multiple user-specific parameters that actually have significance on determining a appropriate gym routine.

GYMY considers:

- Age
- Workout Duration
- Fitness Goal
- Experience Level
- Workout Frequency
- Available Equipment
- Injury Information

The Software generates multiple workout routines and the user can select and view any of them.
## 📚 Documentation

Detailed documentation has been split into separate files for easier navigation.

- 🚀 [Installation Guide](docs/install.md)
- 📖 [Usage Guide](docs/usage.md)
- 🏗️ [Architecture](docs/architecture.md)
- 🔗 [API Documentation](docs/apidocument.md)
---

# ✨ Features

- Personalized workout recommendations
- FastAPI
- React frontend
- MySQL database
- Docker Compose support
- Responsive user interface
- Input validation using Pydantic
- Rule-based recommendation engine

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PyMySQL

## Frontend

- React
- Vite
- Axios
- CSS

## Database

- MySQL

## DevOps

- Docker
- Docker Compose

## Development Tools

- Visual Studio Code
- Git
- GitHub

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
│   │     ├── styles/
│   │     │        └── app.css
│   │     ├── services/
│   │     │        └── api.js
│   │     ├── components/
│   │     │        ├── F.jsx
│   │     │        ├── I.jsx
│   │     │        └── R.jsx
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

# 🌐 Application URLs

Frontend

```
http://localhost:5173
```

Backend API

```
http://localhost:8000
```
---
# ⚙️ Recommendation Modes

The recommendation engine generates multiple workout routines instead of returning a single fixed plan.

### Beginner Friendly
Prioritizes simple compound movements and machine-based exercises.

### Balanced Routine
Provides a mix of compound and isolation exercises.

### Intensive Routine
Includes higher training volume for experienced users.

Users can browse all generated routines and choose the one that best matches their preference.
---

# 🗄 Database Setup

The application uses MySQL.

When Docker Compose is executed:

- MySQL container starts automatically.
- Database is created automatically.
- SQL initialization script imports the dataset.
- Backend connects automatically.

No manual database setup is required.
---
# ⚙️ Request Flow

The React frontend never communicates directly with the MySQL database.

All requests follow this path:

React Frontend
→ FastAPI Backend
→ Recommendation Engine
→ MySQL Database

This separation ensures:

- Better security
- Validation through FastAPI
- Easier maintenance
- Loose coupling between frontend and database
---
# 🚀 How To Use

1. Start the application using Docker Compose.
2. Open your browser.

```
http://localhost:5173
```

3. Fill in the workout form.

Enter:

- Age
- Workout Duration
- Fitness Goal
- Experience Level
- Workout Days Per Week
- Available Equipment
- Injury Information

4. Click the **Generate Workout** button.
5. The React frontend sends your preferences to the FastAPI backend.
6. The backend validates the request using Pydantic.
7. The recommendation engine queries the MySQL database.
8. Matching exercises are selected according to the user's preferences.
9. The personalized workout routine plans are displayed on the screen.
10. Choose from one of the displayed routines, you can see all the routines one by one in any order.

To test the backend directly, open:

```
http://localhost:8000/docs
```

Swagger UI allows testing every endpoint without using the frontend.

---

# ⚙️ How the Recommendation Engine Works

1. User submits workout preferences.
2. FastAPI validates incoming data.
3. Recommendation engine loads exercise data from MySQL.
4. Exercises are filtered according to:
   - Fitness Goal
   - Experience Level
   - Workout Duration
   - Workout Frequency
   - Equipment Availability
   - Injury Information
5. Matching exercises are grouped into a workout plan.
6. Results are returned as JSON.
7. React displays the workout routines.

---

# 👤 User Inputs

The recommendation engine considers:

- Age
- Workout Duration
- Experience Level
- Fitness Goal
- Workout Days Per Week
- Available Equipment
- Injury Information

These inputs allow the system to generate personalized workout plans instead of displaying generic exercise lists.

---

# ✔ Validation

The backend validates all requests using Pydantic.

Examples include:

- Missing fields
- Invalid values
- Incorrect data types
- Empty requests

Appropriate HTTP status codes are returned whenever validation fails.

---

# 🐳 Docker Architecture

The project consists of three independent containers.

### Frontend

- React
- Vite

### Backend

- FastAPI
- Recommendation Engine

### Database

- MySQL

Docker Compose automatically creates the network and allows communication between all containers.

---

# 📊 Dataset Source

Dataset used:

**Gym Exercise Dataset**

Author:
**Niharika Pandit**

Source:

https://www.kaggle.com/datasets/niharika41298/gym-exercise-data

The dataset was cleaned and transformed before being imported into MySQL.

---

# 📸 Screenshots

### User Input Form

![Form](Screenshots/1.png)

### Routine Selection

![Routine Selection](Screenshots/4.png)

### Workout Recommendation

![Recommendation](Screenshots/2.png)


![Swagger](Screenshots/3.png)

---

# 🔮 Future Improvements

- User authentication
- Workout history
- Progress tracking
- Nutrition recommendations
- Exercise videos
- Cloud deployment
- Mobile application
---

# 👨‍💻 Author

**Aadarsh**

GitHub:

https://github.com/AadarshAadi

---

# 🙏 Acknowledgements

This project was developed as part of a technical recruitment assessment.

Open-source technologies used:

- FastAPI
- React
- Docker
- MySQL
- SQLAlchemy
- Pydantic
- Vite
- Axios

Special thanks to the open-source community and Kaggle for providing the dataset used in this project.

---
# 📖 Declaration

For fully transparency, I have used ChatGPT to help speed up some of the repetitive tasks in this project:
- **Debugging MySQL bugs:** MySQL setup through docker was causing errors repeatedly, I used ChatGPT to solve those errors.
- **Syntax Generation:** Some complex syntax of workout filtering logic in the Engine.py were written by ChatGPT, the logic was given by me, the syntax code was taken and pasted in the engine.py. CSS styling and Frontend Allignment was referred through ChatGPT.
- **Proofreading:** I also used ChatGPT to check grammar in this README and also be grammetically correct while writting DOCSTRINGS AND JSDOCS.

Everything else—the rules of recommendation, the pre-processing techniques, the React frontend design, and the Docker container logic—was built by me.