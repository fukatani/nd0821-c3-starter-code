import dataclasses
import pickle

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from starter.ml.data import process_data

app = FastAPI()
model = pickle.load(open("model/trained_model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}


@dataclasses.dataclass
class Data(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    occupation: str
    relationship: str
    race: str
    sex: str
    education_num: int = Query(..., alias="education-num")
    marital_status: str = Query(..., alias="marital-status")
    capital_gain: int = Query(..., alias="capital-gain")
    capital_loss: int = Query(..., alias="capital-loss")
    hours_per_week: int = Query(..., alias="hours-per-week")
    native_country: str = Query(..., alias="native-country")

@app.post("/inference/")
async def exercise_function(data: Data):
    if data.capital_gain < 0:
        raise HTTPException(status_code=400, detail="capital_gain must not be negative")
    if data.capital_loss < 0:
        raise HTTPException(status_code=400, detail="capital_loss must not be negative")
    if data.hours_per_week < 0 or data.hours_per_week > 168:
        raise HTTPException(status_code=400, detail="hours_per_week must be between 0 and 168")
    if data.race not in ["white", "black", "asian-pac-islander", "amer-indian-eskimo", "other"]:
        raise HTTPException(status_code=400, detail="Unexpected race")

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]
    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=None,
    )
    pred = model.predict(X)
    return {"saraly": pred}
