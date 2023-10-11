from fastapi.testclient import TestClient

from src.main import app  # Import your FastAPI app

client = TestClient(app)


def test_hello_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
