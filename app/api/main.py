from fastapi import FastAPI, HTTPException
from app.models.task_models import TaskEvaluationRequest, TaskEvaluationList
from app.services.task_evaluator import TaskEvaluator

app = FastAPI(
    title="Task Load Estimation API",
    description="API for estimating cognitive load of tasks based on keyword analysis",
    version="1.0.0"
)

@app.post("/evaluate", response_model=TaskEvaluationList)
async def evaluate_tasks(request: TaskEvaluationRequest):
    try:
        evaluations = TaskEvaluator.evaluate_tasks(
            tasks=request.tasks,
            should_validate=request.should_validate
        )
        return TaskEvaluationList(evaluations=evaluations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 