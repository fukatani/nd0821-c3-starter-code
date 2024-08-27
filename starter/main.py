import pickle

from fastapi import FastAPI, HTTPException
import pandas
from pydantic import BaseModel, Field

from training.ml.data import process_data

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

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "age": 20,
                    "workclass": "State-gov",
                    "fnlgt": 77516,
                    "education": "HS-grad",
                    "education-num": 9,
                    "marital-status": "Divorced",
                    "occupation": "Handlers-cleaners",
                    "relationship": "Not-in-family",
                    "race": "Asian-Pac-Islander",
                    "sex": "Male",
                    "capital-gain": 2174,
                    "capital-loss": 0,
                    "hours-per-week": 40,
                    "native-country": "United-States",
                }
            ]
        }
    }


@app.post("/inference/")
async def exercise_function(data: Data):
    if data.capital_gain < 0:
        raise HTTPException(status_code=400, detail="capital-gain must not be negative")
    if data.capital_loss < 0:
        raise HTTPException(status_code=400, detail="capital-loss must not be negative")
    if data.hours_per_week < 0 or data.hours_per_week > 168:
        raise HTTPException(
            status_code=400, detail="hours-per-week must be between 0 and 168"
        )
    if data.race not in [
        "White",
        "Black",
        "Asian-Pac-Islander",
        "Amer-Indian-Eskimo",
        "Other",
    ]:
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

    df = pandas.DataFrame(
        {
            "age": [
                data.age,
            ],
            "workclass": [
                data.workclass,
            ],
            "fnlgt": [
                data.fnlgt,
            ],
            "education": [
                data.education,
            ],
            "education-num": [
                data.education_num,
            ],
            "marital-status": [
                data.marital_status,
            ],
            "occupation": [
                data.occupation,
            ],
            "relationship": [
                data.relationship,
            ],
            "race": [
                data.race,
            ],
            "sex": [
                data.sex,
            ],
            "capital-gain": [
                data.capital_gain,
            ],
            "capital-loss": [
                data.capital_loss,
            ],
            "hours-per-week": [
                data.hours_per_week,
            ],
            "native-country": [
                data.native_country,
            ],
            # 'salary': ["",],
        },
    )
    X, _, _, _ = process_data(
        df,
        categorical_features=cat_features,
        # label="salary",
        training=False,
        encoder=encoder,
        lb=None,
    )
    pred = model.predict(X)
    return {"salary": float(pred)}
