import os
import sys

# Set test environment variables BEFORE importing the app
os.environ["MONGO_URI"] = "mongodb://localhost:27017/testdb"
os.environ["SECRET_KEY"] = "test-secret-key-that-is-very-long-and-secure-2026!"
os.environ["ALLOWED_ORIGINS"] = "http://localhost:3000,http://localhost:5173"
os.environ["JWT_SECRET_KEY"] = "test-secret-key-that-is-very-long-and-secure-2026!"
os.environ["JWT_REFRESH_SECRET_KEY"] = "test-refresh-key-that-is-very-long-and-secure-2026!"

import pytest
from fastapi.testclient import TestClient

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert "HealthSense AI API" in response.json()["service"]

def test_auth_me_unauthorized(client):
    response = client.get("/auth/me")
    assert response.status_code == 401

def test_auth_login_invalid_credentials(client):
    payload = {
        "email": "wrong_tester@healthsense.ai",
        "password": "WrongPassword@123"
    }
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"

def test_auth_register_validation_error(client):
    # Test invalid email and weak password (missing symbols/numbers/uppercase)
    payload = {
        "name": "T",
        "email": "notanemail",
        "password": "pass"
    }
    response = client.post("/auth/register", json=payload)
    assert response.status_code == 422
