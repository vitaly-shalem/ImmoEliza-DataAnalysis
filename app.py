from pathlib import Path
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json

from src.api.check import check_input_data
from src.api.preprocessing import process_property_data
from src.api.predict import predict_price

paths = dict()
paths["transformer"] = Path.cwd() / "models" / "transformer.dat"
paths["scaler"] = Path.cwd() / "models" / "scaler.dat"
paths["model"] = Path.cwd() / "models" / "xgbreg_model.dat"

app = FastAPI()

class PropertyData(BaseModel):
    type: str="HOUSE|APARTMENT"
    region: str="Brussels|Flanders|Wallonie"
    province: str="Brussels|Antwerp|East Flanders|Flemish Brabant|Limburg|West Flanders|Hainaut|Namur|Luxembourg|Liège|Walloon Brabant"
    district: str="Aalst|Antwerp|Arlon|Ath|Bastogne|Brugge|Brussels|Charleroi|Dendermonde|..."
    postalCode: str="1000|2000|9000|..."
    locality: str="Brussels|Antwerpen|Gent|..."
    bedroomCount: int
    netHabitableSurface: float
    condition: str="NEW|AS_NEW|JUST_RENOVATED|GOOD|TO_BE_DONE_UP|TO_RENOVATE|TO_RESTORE|UNKNOWN"
    epcScore: str="A|B|C|D|E|F|G"
    bathroomCount: int
    showerRoomCount: int
    toiletCount: int
    hasLift: bool=False
    fireplaceExists: bool=False
    hasSwimmingPool: bool=False
    hasAirConditioning: bool=False
    hasGarden: bool=False
    hasTerrace: bool=False
    gardenSurface: float
    terraceSurface: float
    land: float

@app.get("/")
def welcome():
    return {"message": "Welcome to Immo Eliza - Real Estate Price Prediction!"}

@app.post("/predict")
def predict(data: PropertyData):
    status = None
    property_data = json.loads(data.json())
    status, errors, property_data = check_input_data(property_data)
    if status == 200:
        price = predict_price(process_property_data(property_data), paths)
        status = 200 if price != None else 404
        return {"prediction": price, "status": status}
    else:
        return errors

# uvicorn app:app --reload