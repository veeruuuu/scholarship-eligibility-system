from fastapi import APIRouter, HTTPException
from app.schemas import StudentInput, EvaluationResult
from app.fuzzy_engine.engine import run_evaluation

router = APIRouter()


@router.post("/api/evaluate", response_model=EvaluationResult)
def evaluate(student: StudentInput):
    if student.semester >= 2 and student.cgpa is None:
        raise HTTPException(status_code=422, detail="CGPA is required for semester 2 and above")

    result = run_evaluation(student)
    return EvaluationResult(**result)

from app.fuzzy_engine.optimization.ga_optimizer import run_ga
from app.schemas import OptimizationResult


@router.post("/api/optimize", response_model=OptimizationResult)
def optimize():
    result = run_ga()
    return OptimizationResult(**result)