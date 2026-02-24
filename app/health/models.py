from pydantic import BaseModel
from typing import Dict

class HealthCheckResult(BaseModel):
    status: str
    checks: Dict[str, str]