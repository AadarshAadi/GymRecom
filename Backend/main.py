from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from engine import datalload, genwork
from schemas import WR
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load exercise data when the application starts."""
    datalload()
    yield
app = FastAPI(title="EngineAPI",version="1.0.0",lifespan=lifespan)
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"],)
@app.get("/")
def home():
    return {
        "message": "GYMY API Running"
    }
@app.post("/recommend")
def recommend(request: WR):
    """Generate a personalized workout plan."""
    result = genwork(workcat=request.workcat,days=request.days,age=request.age,duration=request.duration,exper=request.exper,equipm=request.equipm,injury=request.injury)
    return result