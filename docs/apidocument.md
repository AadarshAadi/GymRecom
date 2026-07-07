# API Documentation

The backend is built using FastAPI.

## Base URL

```
http://localhost:8000
```

## Interactive Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

## Main Endpoint

### Generate Workout Recommendation

**POST**

```
/
```

### Request Body

```json
{
  "age": 22,
  "duration": 60,
  "goal": "Muscle Gain",
  "experience": "Beginner",
  "days_per_week": 5,
  "equipment": "Gym",
  "injury": "None"
}
```

### Response

```json
[
  {
    "routine_name": "Routine A",
    "exercises": [
      ...
    ]
  }
]
```

## Validation

The backend validates:

- Required fields
- Data types
- Invalid values
- Empty requests

Validation is implemented using **Pydantic**.