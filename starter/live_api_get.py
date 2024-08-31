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

response = requests.get(
    "https://nd0821-c3-starter-code2-532522952365.us-central1.run.app/",
    headers=headers,
)

print(response.status_code)
print(response.json())
