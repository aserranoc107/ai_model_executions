from app.api.health import router as health_router
from fastapi import FastAPI, HTTPException
from app.models import ExecutionCreate
import app.repository as repo

app = FastAPI()

app.include_router(health_router)

@app.get("/executions")
def get_executions():
    return repo.get_all_executions()

@app.post("/executions")
def create_execution(execution:ExecutionCreate):
    new_id = repo.create_execution(execution.dict())
    return {"id": new_id}

@app.put("executions/{execution_id}")
def update_execution(execution_id: int, execution: ExecutionCreate):
    update = repo.update_execution(execution_id, execution.dict())

    if update == 0:
        raise HTTPException(status_code=404, detail="Not found")
    
    return {"message": "successfully updated"}

