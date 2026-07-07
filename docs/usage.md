# Usage Guide

This guide explains how to use Gymy to generate personalized workout routines.

---

# Getting Started

Before using the application, ensure all services are running. If you haven't installed the project yet, follow the [Installation Guide](install.md).

Open your browser and navigate to:

```
http://localhost:5173
```

---

# Generating a Workout Plan

1. Open the Gymy application.
2. Fill in the workout preference form.
3. Click the **Generate Workout** button.
4. Wait for the recommendation engine to process your request.
5. Browse the generated workout routines.
6. Select any routine to view its complete exercise plan.

---

# User Inputs

The recommendation engine generates personalized routines based on the following information:

| Input | Description |
|--------|-------------|
| Age | User's age |
| Workout Duration | Desired duration of each workout session |
| Fitness Goal | Muscle Gain, Weight Loss, Strength, etc. |
| Experience Level | Beginner, Intermediate, or Advanced |
| Workout Days Per Week | Number of training days |
| Available Equipment | Gym equipment available to the user |
| Injury Information | Existing injuries or physical limitations |

Providing accurate information helps the system generate more suitable workout recommendations.

---

# How Recommendations Are Generated

After submitting the form, the application follows the workflow below:

1. The React frontend sends your preferences to the FastAPI backend.
2. FastAPI validates the incoming request using Pydantic.
3. The recommendation engine retrieves exercise data from the MySQL database.
4. Exercises are filtered based on your preferences.
5. Matching exercises are grouped into complete workout routines.
6. The generated routines are returned to the frontend.
7. The recommended workout plans are displayed for you to explore.

---

# Recommendation Criteria

The recommendation engine considers several factors while generating workout plans, including:

- Fitness Goal
- Experience Level
- Workout Duration
- Workout Frequency
- Equipment Availability
- Injury Information
- Age

By combining these inputs, Gymy generates workout routines tailored to each user's requirements instead of displaying generic exercise lists.

---

# Viewing the Results

Once recommendations are generated, you can:

- Browse multiple workout routines.
- View exercises included in each routine.
- Compare different routines before choosing one.
- Explore every generated plan without submitting the form again.

---

# Testing the Backend Directly

The backend provides interactive API documentation through Swagger UI.

Open:

```
http://localhost:8000/docs
```

Swagger UI allows you to test every API endpoint without using the frontend application.

Alternatively, ReDoc documentation is available at:

```
http://localhost:8000/redoc
```

---

# Input Validation

All incoming requests are validated using **Pydantic**.

Examples of validation include:

- Missing required fields
- Invalid values
- Incorrect data types
- Empty requests

If validation fails, the API returns an appropriate HTTP error response with details about the issue.