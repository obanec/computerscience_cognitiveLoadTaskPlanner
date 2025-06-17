# Task Load Estimation API

This project provides a lightweight RESTful API for estimating the cognitive load of user-defined tasks. The system uses a simple heuristic model to classify tasks as low, medium, or high cognitive demand, and optionally validates input with a Large Language Model (LLM).

---

## 🚀 Features

- Accepts free-form task descriptions.
- Classifies each task by cognitive load: `low`, `medium`, or `high`.
- Optional validation using OpenAI's GPT API.
- Designed as a microservice (FastAPI + Docker).
- Ready for integration into productivity or planning tools.

---

## 📦 Tech Stack

- Python 3.10
- FastAPI
- Uvicorn
- Pydantic
- Docker
- Optional: OpenAI API for task validation

---

## 📥 Installation

### Run locally (development)

```bash
pip install -r requirements.txt
uvicorn app.api.main:app --reload