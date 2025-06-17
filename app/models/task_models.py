from pydantic import BaseModel
from typing import List, Optional

class TaskEvaluationRequest(BaseModel):
    tasks: List[str]
    should_validate: bool = False

class TaskEvaluationResponse(BaseModel):
    task: str
    valid: bool
    load: str

class TaskEvaluationList(BaseModel):
    evaluations: List[TaskEvaluationResponse] 