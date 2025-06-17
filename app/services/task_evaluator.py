from typing import List
from app.models.task_models import TaskEvaluationResponse

class TaskEvaluator:
    # Keywords that indicate different levels of cognitive load
    HIGH_LOAD_KEYWORDS = {
        'write', 'analyze', 'design', 'create', 'develop', 'implement',
        'solve', 'calculate', 'plan', 'strategize', 'research', 'present'
    }
    
    MEDIUM_LOAD_KEYWORDS = {
        'review', 'check', 'verify', 'organize', 'sort', 'compile',
        'prepare', 'update', 'modify', 'adjust', 'coordinate'
    }
    
    LOW_LOAD_KEYWORDS = {
        'wash', 'clean', 'move', 'carry', 'lift', 'walk', 'run',
        'stand', 'sit', 'wait', 'watch', 'listen'
    }

    @classmethod
    def evaluate_tasks(cls, tasks: List[str], should_validate: bool = False) -> List[TaskEvaluationResponse]:
        evaluations = []
        
        for task in tasks:
            task_lower = task.lower()
            words = set(task_lower.split())
            
            # Determine cognitive load based on keywords
            load = "medium"  # default
            if any(keyword in words for keyword in cls.HIGH_LOAD_KEYWORDS):
                load = "high"
            elif any(keyword in words for keyword in cls.LOW_LOAD_KEYWORDS):
                load = "low"
            
            # Basic validation (can be expanded)
            valid = True
            if should_validate:
                valid = len(task.strip()) > 0 and len(task) <= 100
            
            evaluations.append(
                TaskEvaluationResponse(
                    task=task,
                    valid=valid,
                    load=load
                )
            )
        
        return evaluations 