from pydantic import BaseModel, Field
from typing import Optional


class StudentInput(BaseModel):
    marks_10th: float = Field(..., ge=0, le=100)
    marks_12th: float = Field(..., ge=0, le=100)
    entrance_obtained: float = Field(..., ge=0)
    entrance_max: float = Field(..., gt=0)
    semester: int = Field(..., ge=1, le=8)
    cgpa: Optional[float] = Field(None, ge=0, le=10)
    annual_income: float = Field(..., ge=0)
    extra_curricular: float = Field(..., ge=0, le=100)
    disability: bool
    hostel_type: str  # "Hosteller" | "Day Scholar"
    location: str      # "Urban" | "Rural"


class ModuleScore(BaseModel):
    score: float
    category: str


class EvaluationResult(BaseModel):
    academic_strength: ModuleScore
    need_score: ModuleScore
    achievement_score: ModuleScore
    final_eligibility: float
    recommendation: str
    activated_rules: list[str]
    key_factors: list[str]
    explanation: str

class OptimizationResult(BaseModel):
    original_boundaries: dict
    optimized_boundaries: dict
    original_mse: float
    optimized_mse: float
    improvement_pct: float
    fitness_history: list[dict]
    sample_count: int