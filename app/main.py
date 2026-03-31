import psycopg2
from app.helpers.ApiResponse import ApiResponse
from app.helpers.logEvents import log_event
from app.helpers.logLevels import ERRORLOGS,INFOLOGS
from app.exceptions.globalException import register_exception_handlers
from app.exceptions.errors import AppError, LLMServiceError
from app.api.health import router as health_router
from fastapi import FastAPI, HTTPException, Request
from app.models import ExecutionCreate
from app.helpers.context import request_id_ctx
import app.services as services
import socket
import uuid

app = FastAPI()
app.include_router(health_router)
instance_id = socket.gethostname()
register_exception_handlers(app)


@app.middleware("http")
async def add_request_id(request:Request, call_next):
    request_id_ctx.set(str(uuid.uuid4()))
    response = await call_next(request)
    return response


@app.get("/executions")
def get_executions():
    try:
        result = services.get_all_executions()
        log_event(INFOLOGS, "Executions GET endpoint", "Success", "Process successfully executed")

        return ApiResponse(
            status="success",
            message="Process completed",
            data={"result": result}
        )

    except psycopg2.OperationalError as ex:
        raise AppError((str(ex)))
  

@app.post("/executions")
def create_execution(execution:ExecutionCreate):
    try:
        new_id = services.create_execution(execution.dict())
        log_event(INFOLOGS, "Executions POST endpoint", "Success", "Creation successfully")

        return ApiResponse(
            status="success",
            message="Process completed",
            data={f"result: {new_id}"}
        )

    except psycopg2.OperationalError as ex:
        raise AppError((str(ex)))

@app.put("executions/{execution_id}")
def update_execution(execution_id: int, execution: ExecutionCreate):
    try:
        update = services.update_execution(execution_id, execution.dict())
        if update == 0:
            log_event(INFOLOGS, "Executions UPDATE endpoint", 404, "Not found")
            raise HTTPException(status_code=404, detail="Not found")

        log_event(INFOLOGS, "Executions UPDATE endpoint", "Success", "Update successfully")
        return {"message": "successfully updated"}
    
    except psycopg2.OperationalError as ex:
        raise AppError((str(ex)))


@app.post("/infer")
async def infer(prompt: str):
    try:
        result = await services.run_model(prompt)
        result = services.clean_response(result)
        services.save_result()

        log_event(INFOLOGS, "Infer endpoint called", "Success", f"Result: {result}")
        
    except psycopg2.OperationalError as ex:
        raise LLMServiceError((str(ex)))

    return {"result": result}