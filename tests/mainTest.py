import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def health_check_test():
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def research_endpoint_test():
    res = client.post('/research', json={})
    assert res.status_code == 422