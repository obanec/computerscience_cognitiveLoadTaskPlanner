# Task Load Estimation API

A RESTful API that estimates the cognitive load of free-form task descriptions using a lightweight heuristic model. Designed for integration into productivity tools and wellness platforms, the API offers fast, interpretable classification with optional validation via a language model.

---

## Features

- Classifies tasks into `low`, `medium`, or `high` cognitive load  
- Rule-based keyword heuristic (fully explainable)  
- Optional semantic validation using an LLM (e.g., OpenAI GPT)  
- Built with FastAPI and Pydantic  
- Interactive documentation with Swagger and ReDoc  
- Docker-ready for deployment as a microservice  
- Health check endpoint (`/health`)  
- Includes basic test suite  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/obanec/computerscience_cognitiveLoadTaskPlanner.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running the API

### Local development
```bash
uvicorn app.api.main:app --reload
```

### Using Docker
```bash
docker build -t task-load-api .
docker run -p 8000:8000 task-load-api
```

---

## API Usage

### POST `/evaluate`

**Request body:**
```json
{
  "tasks": ["write report", "wash dishes"],
  "should_validate": false
}
```

**Response:**
```json
[
  { "task": "write report", "valid": true, "load": "high" },
  { "task": "wash dishes", "valid": true, "load": "low" }
]
```

---

### GET `/health`

Returns 200 OK if the service is live.

---

## Running Tests

```bash
pytest tests/
```

---

## API Documentation

Once the server is running, access:

- Swagger UI → http://localhost:8000/docs  
- ReDoc → http://localhost:8000/redoc  

---

## Project Structure

```
task_load_api/
├── app/
│   ├── api/           # FastAPI entrypoint
│   ├── models/        # Request/response schemas
│   ├── services/      # Load classification logic
│   └── core/          # Reserved for future configs
├── tests/             # Unit and integration tests
├── Dockerfile         # Container configuration
├── requirements.txt   # Project dependencies
```

