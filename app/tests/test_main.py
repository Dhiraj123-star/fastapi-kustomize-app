from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_healthz_endpoint():
    """Test the /healthz endpoint returns a successful status"""
    response = client.get("/healthz")
    assert response.status_code==200
    assert response.json()["status"]=="Ok"