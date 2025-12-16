from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root_endpoint():
    """Test the root endpoint (/) returns a 200 status and the expected message."""
    response = client.get("/")
    
    # Assert HTTP success
    assert response.status_code == 200
    
    # Assert the hardcoded message in main.py
    assert response.json()["message"] == "Hello from FastAPI + Docker + Kustomize + Github Actions!!"