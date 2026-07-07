# System Architecture

This document describes the overall architecture of Gymy, including the software components, data flow, dataset preprocessing, and the rule-based recommendation engine.

---

# Overall Architecture

The application follows a three-tier architecture consisting of a frontend, backend, and database.

```text
                     User
                       │
                       ▼
                React Frontend
                       │
             HTTP REST API Requests
                       │
                       ▼
                FastAPI Backend
                       │
              Request Validation
                  (Pydantic)
                       │
                       ▼
        Rule-Based Recommendation Engine
                       │
             SQLAlchemy + Pandas
                       │
                       ▼
                MySQL Database
```

---

# Component Overview

## Frontend

The frontend is built using **React** with **Vite** and provides the user interface.

Its responsibilities include:

- Collecting workout preferences
- Sending requests to the backend
- Displaying generated workout routines
- Presenting multiple workout variations

---

## Backend

The backend is developed using **FastAPI**.

Its responsibilities include:

- Receiving user requests
- Validating inputs using Pydantic
- Executing recommendation logic
- Returning personalized workout plans as JSON

---

## Database

The application uses a MySQL database containing a cleaned exercise dataset.

Each exercise record stores information such as:

- Exercise Name
- Target Muscle
- Difficulty Level
- Equipment Required

The backend loads this dataset into memory using Pandas during application startup, reducing repeated database queries while generating workout plans.

---

# Recommendation Engine Architecture

Unlike machine learning-based recommender systems, Gymy uses a **rule-based recommendation engine**.

Instead of predicting workouts using a trained model, the engine applies predefined fitness rules to generate personalized workout plans.

The workflow is shown below.

```text
             User Preferences
                    │
                    ▼
           Input Validation
                    │
                    ▼
       Determine Workout Category
                    │
                    ▼
         Select Workout Split
                    │
                    ▼
      Load Training Profile Rules
                    │
                    ▼
     Calculate Exercises per Session
                    │
                    ▼
    Apply Injury & Equipment Filters
                    │
                    ▼
       Select Suitable Exercises
                    │
                    ▼
       Generate Weekly Workout Plan
                    │
                    ▼
        Return Multiple Variations
```

---

# Recommendation Logic

The recommendation engine generates workout plans using several rule sets.

## 1. Workout Split Selection

The engine first determines the most appropriate workout split based on:

- Fitness Goal
- Training Days Per Week

For example:

| Goal | Days | Split |
|------|------|-------|
| Hypertrophy | 3 | Push Pull Legs |
| Hypertrophy | 5 | Bro Split |
| Strength | 4 | Upper Lower Strength |

---

## 2. Training Profile Selection

A predefined training profile is selected according to the user's:

- Experience Level
- Workout Category

Each profile specifies:

- Number of sets
- Repetition range
- Rest duration
- Warm-up duration
- Cool-down duration
- Transition time

This ensures that workout intensity scales appropriately with experience.

---

## 3. Exercise Count Estimation

Instead of assigning a fixed number of exercises, the engine estimates how many exercises can fit into the selected workout duration.

The calculation considers:

- Warm-up time
- Cool-down time
- Number of sets
- Average repetitions
- Rest intervals
- Transition time between exercises

This produces workout sessions that realistically fit within the user's available time.

---

## 4. Exercise Filtering

The engine filters exercises using multiple criteria.

### Experience Level

Exercises are filtered according to the user's experience.

For example:

- Beginners only receive beginner-friendly exercises.
- Intermediate users receive beginner and intermediate exercises.
- Advanced users can access all difficulty levels.

---

### Equipment Availability

Only exercises compatible with the user's available equipment are considered.

---

### Injury Restrictions

The recommendation engine removes exercises that may aggravate existing injuries.

Examples include:

- Knee pain
- Lower back pain
- Shoulder pain

Exercises containing restricted keywords are automatically excluded from the recommendation process.

---

## 5. Workout Plan Generation

After filtering, the engine:

- Selects exercises for each muscle group.
- Builds a complete weekly workout schedule.
- Generates three different workout variations by selecting different exercise combinations.

This allows users to choose from multiple valid workout routines rather than receiving a single recommendation.

---

# Dataset Preprocessing

The exercise dataset was cleaned before being imported into MySQL.

## Data Cleaning

The following preprocessing steps were performed:

- Removed duplicate records.
- Removed incomplete entries.
- Removed invalid exercises.
- Removed unnecessary columns.
- Standardized missing values.
- Cleaned whitespace and inconsistent formatting.

---

## Data Structuring

After cleaning, the dataset was organized into a relational MySQL table.

The data was then exported as an SQL initialization script, allowing Docker Compose to automatically populate the database during startup.

---

## Why Preprocessing Was Necessary

The recommendation engine relies heavily on consistent attribute values such as:

- Muscle group
- Equipment
- Difficulty level

Cleaning and standardizing these fields ensures accurate filtering and prevents invalid recommendations.

---

# Data Flow

The overall request flow is illustrated below.

```text
User
 │
 ▼
React Frontend
 │
 ▼
FastAPI API Endpoint
 │
 ▼
Pydantic Validation
 │
 ▼
Recommendation Engine
 │
 ├── Determine workout split
 ├── Load training profile
 ├── Calculate exercise count
 ├── Apply equipment filters
 ├── Apply injury filters
 ├── Select exercises
 └── Build weekly routine
 │
 ▼
JSON Response
 │
 ▼
React Frontend
 │
 ▼
Workout Recommendation Display
```