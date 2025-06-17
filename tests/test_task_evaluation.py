from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)

def test_evaluate_tasks():
    # Test data
    test_tasks = {
        "tasks": ["write report", "wash dishes", "review documents"],
        "should_validate": True
    }
    
    # Make request to the API
    response = client.post("/evaluate", json=test_tasks)
    
    # Assert response status code
    assert response.status_code == 200
    
    # Assert response structure
    data = response.json()
    assert "evaluations" in data
    assert len(data["evaluations"]) == 3
    
    # Assert specific task evaluations
    evaluations = {e["task"]: e for e in data["evaluations"]}
    
    assert evaluations["write report"]["load"] == "high"
    assert evaluations["wash dishes"]["load"] == "low"
    assert evaluations["review documents"]["load"] == "medium"
    
    # Assert all tasks are valid
    assert all(e["valid"] for e in data["evaluations"])

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"} 