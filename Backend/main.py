from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from engine import load_dataset
from engine import generate_workout
from schemas import WR
app = FastAPI(
    title="Workout Recommendation API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup():
    load_dataset()
@app.get("/")
def home():
    return {
        "message": "Workout Recommendation API Running"
    }


@app.post("/recommend")
def recommend(request: WR):

    result = generate_workout(
        workout_type=request.workout_type,
        days=request.days,
        age=request.age,
        duration=request.duration,
        experience_level=request.experience_level,
        available_equipment=request.available_equipment,
        injury=request.injury
    )

    return result