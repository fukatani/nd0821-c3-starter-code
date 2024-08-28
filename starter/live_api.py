import requests

response = requests.post(
    "http://127.0.0.1:7000/inference/",
    json={
        "age": 20,
        "capital-gain": 2174,
        "capital-loss": 0,
        "education": "HS-grad",
        "education-num": 9,
        "fnlgt": 77516,
        "hours-per-week": 40,
        "marital-status": "Divorced",
        "native-country": "United-States",
        "occupation": "Handlers-cleaners",
        "race": "Asian-Pac-Islander",
        "relationship": "Not-in-family",
        "sex": "Male",
        "workclass": "State-gov",
    },
)

print(response.status_code)
print(response.json())
