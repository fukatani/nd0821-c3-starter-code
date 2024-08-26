import pickle

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from starter.starter.ml.data import process_data

app = FastAPI()
model = pickle.load(open("model/trained_model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}


class Data(BaseModel):
    age: int
    workclass: str
    fnlgt: int
    education: str
    occupation: str
    relationship: str
    race: str
    sex: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: str = Field(alias="native-country")


@app.post("/inference/")
async def exercise_function(data: Data):
    if data.capital_gain < 0:
        raise HTTPException(status_code=400, detail="capital-gain must not be negative")
    if data.capital_loss < 0:
        raise HTTPException(status_code=400, detail="capital-loss must not be negative")
    if data.hours_per_week < 0 or data.hours_per_week > 168:
        raise HTTPException(status_code=400, detail="hours-per-week must be between 0 and 168")
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
