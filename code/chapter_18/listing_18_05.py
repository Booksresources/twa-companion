# Listing 18.5: Testing the API
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)
r = client.post(
    "/classify", json={"text": "OPEC ministers agreed to cut crude oil output."}
)
print(r.status_code, r.json())
r = client.post("/classify", json={"text": "short"})
print(r.status_code, r.json()["detail"][0]["msg"])
