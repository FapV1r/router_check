from fastapi import FastAPI

from .database import engine, Base
from .routers import sensors, readings
from . import models


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sensors.router)
app.include_router(readings.router)

@app.get("/")
def root():
    return {"message": "SmartDorm"}
