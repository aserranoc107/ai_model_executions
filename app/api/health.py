from fastapi import APIRouter, HTTPException
from app.health.service import HealthService
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="",
    tags=["Health"]
)
health_service = HealthService()

@router.get("/health")
def health():
    return {"status": "alive"}

@router.get("/ready")
def readiness():
    result = health_service.run_checks()

    if result.status != "ready":
        raise HTTPException(status_code=503, detail=result.dict())

    return result