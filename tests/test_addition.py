from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_addition_success():
    request_data = {
        "batchid": "id0101",
        "payload": [[1, 2], [3, 4]]
    }
    response = client.post("/api/add", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == [3, 7]
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data

def test_addition_invalid_payload():
    request_data = {
        "batchid": "id0101",
        "payload": [[1, "a"], [3, 4]]
    }
    response = client.post("/api/add", json=request_data)
    assert response.status_code == 422

def test_addition_empty_payload():
    request_data = {
        "batchid": "id0101",
        "payload": []
    }
    response = client.post("/api/add", json=request_data)
    assert response.status_code == 200
    data = response.json()
    assert data["batchid"] == "id0101"
    assert data["response"] == []
    assert data["status"] == "complete"
    assert "started_at" in data
    assert "completed_at" in data
