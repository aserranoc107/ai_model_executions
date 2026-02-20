from fastapi import APIRouter, HTTPException
from app.health.service import HealthService
from fastapi.responses import JSONResponse

router = APIRouter()
health_service = HealthService()

@router.get("/health")
def health():
    return {"status": "alive"}

@router.get("/ready")
def readiness():
    result = health_service.run_checks()

    if result.status != "ready":
        raise JSONResponse(status_code=503, content=result.dict())

    return result