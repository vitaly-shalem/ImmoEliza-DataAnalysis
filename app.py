from pathlib import Path
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json

from src.preprocessing import *
from src.predict import *

paths = dict()
paths["transformer"] = Path.cwd() / "models" / "transformer.dat"
paths["scaler"] = Path.cwd() / "models" / "scaler.dat"
paths["model"] = Path.cwd() / "models" / "xgbreg_model.dat"

app = FastAPI()

class PropertyData(BaseModel):
    type: str
    region: str
    province: str
    district: str
    postalCode: str
    locality: str
    bedroomCount: int
    netHabitableSurface: float
    condition: str
    epcScore: str
    bathroomCount: int
    showerRoomCount: int
    toiletCount: int
    hasLift: bool
    fireplaceExists: bool
    hasSwimmingPool: bool
    hasAirConditioning: bool
    hasGarden: bool
    hasTerrace: bool
    gardenSurface: float
    terraceSurface: float
    land: float


@app.get("/")
def welcome():
    return {"message": "Welcome to Immo Eliza - Real Estate Price Prediction!"}

@app.post("/predict")
def predict(data: PropertyData):
    property_data = json.loads(data.json())
    price = predict_price(process_property_data(property_data), paths)
    status = 200 if price != None else 401
    return {"prediction": price, "status": status}


# uvicorn app:app --reload