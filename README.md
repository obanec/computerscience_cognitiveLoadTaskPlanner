# Task Load Estimation API

A REST API that estimates the cognitive load of tasks based on keyword analysis.

## Features

- Evaluates tasks and classifies them as low, medium, or high cognitive load
- Simple keyword-based heuristic approach
- Input validation support
- Docker support
- Health check endpoint

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

## Running the API

### Local Development
```bash
python3 -m uvicorn app.api.main:app --reload
```

### Using Docker
```bash
docker build -t task-load-api .
docker run -p 8000:8000 task-load-api
```

## API Usage

### Evaluate Tasks
```bash
curl -X POST "http://localhost:8000/evaluate" \
     -H "Content-Type: application/json" \
     -d '{
           "tasks": ["write report", "wash dishes"],
           "should_validate": false
         }'
```

### Health Check
```bash
curl "http://localhost:8000/health"
```

## Running Tests
```bash
pytest tests/
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc