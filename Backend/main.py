from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from engine import datalload
from engine import genwork
from schemas import WR
app = FastAPI(
    title="EngineAPI",
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
    datalload()
@app.get("/")
def home():
    return {
        "message": "Workout Recommendation API Running"
    }
@app.post("/recommend")
def recommend(request: WR):
    result = genwork(
        workcat=request.workcat,
        days=request.days,
        age=request.age,
        duration=request.duration,
        exper=request.exper,
        equipm=request.equipm,
        injury=request.injury
    )
    return result