import pickle

import pandas
import pytest
from starter.starter.ml.data import process_data


@pytest.fixture(scope="session")
def data():
    df = pandas.read_csv("data/cleaned_census.csv", low_memory=False)
    return df.head(10)


@pytest.fixture(scope="session")
def model():
    return pickle.load(open("model/trained_model.pkl", "rb"))


@pytest.fixture(scope="session")
def encoder():
    return pickle.load(open("model/encoder.pkl", "rb"))


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


def test_pred_shape(data, model, encoder):
    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=None,
    )
    pred = model.predict(X)
    assert pred.shape == (10,)


def test_pred_value(data, model, encoder):
    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=None,
    )
    pred = model.predict(X)
    assert ((pred == 0) | (pred == 1)).all()


def test_encode_shape(data, encoder):
    X, _, _, _ = process_data(
        data,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=None,
    )
    assert X.shape == (10, 109)
