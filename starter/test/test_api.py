from fastapi.testclient import TestClient

from starter.main import app, Data

client = TestClient(app)


def test_get_greeting():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}


def test_inference_error():
    json_body = {
        "age": 20,
        "workclass": "State-gov",
        "fnlgt": 77516,
        "education": "Bachelors",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "education-num": 13,
        "marital-status": "Never-married",
        "capital-gain": -40,
        "capital-loss": 40,
        "hours-per-week": 40,
        "native-country": "United-States",
    }
    r = client.post("/inference", json=json_body)
    assert r.status_code == 400
    assert r.json() == {"detail": "capital-gain must not be negative"}


def test_inference():
    json_body = {
        "age": 20,
        "workclass": "State-gov",
        "fnlgt": 77516,
        "education": "Bachelors",
        "occupation": "Adm-clerical",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "education-num": 13,
        "marital-status": "Never-married",
        "capital-gain": 0,
        "capital-loss": 40,
        "hours-per-week": 40,
        "native-country": "United-States",
    }
    r = client.post("/inference", json=json_body)
    assert r.status_code == 400
    assert r.json() == {"detail": "capital-gain must not be negative"}
