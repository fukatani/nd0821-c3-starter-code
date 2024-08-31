import google.auth
from google.auth.transport.requests import Request
import requests

credentials, project_id = google.auth.default()
credentials.refresh(Request())
token = credentials.token
# print(token)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://nd0821-c3-starter-code2-532522952365.us-central1.run.app/inference/",
    headers=headers,
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
