from fastapi import Request
from fastapi.responses import JSONResponse
from app.helpers.logEvents import log_event
from .errors import DataServiceError, ExternalServiceError, LogicServiceError, LLMServiceError
from app.helpers.logLevels import ERRORLOGS


def register_exception_handlers(app):

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        
        if isinstance(exc, DataServiceError):
            event = "db.error"
            log_event(
                ERRORLOGS,
                status_code= 409,
                status="error",
                event = event,
                message=str(exc)
            )
            return JSONResponse(status_code=502, content={"details": event})

        elif isinstance(exc, ExternalServiceError):
            event = "external.error"
            log_event(
                ERRORLOGS,
                status_code= 502,
                status="error",
                event = event,
                message=str(exc)
            )
            return JSONResponse(status_code=502, content={"details": event})
        
        elif isinstance(exc, LLMServiceError):
            event = "llm.service.error"
            log_event(
                ERRORLOGS,
                status_code= 502,
                status="error",
                event = event,
                message=str(exc)
            )
            return JSONResponse(status_code=502, content={"details": event})
        
        elif isinstance(exc, LogicServiceError):
            event = "service.logical.error"
            log_event(
                ERRORLOGS,
                status_code= 500,
                status="error",
                event = event,
                message=str(exc)
            )
            return JSONResponse(status_code=502, content={"details": event})

        else:
            event = "internal.error"
            log_event(
                ERRORLOGS,
                status_code= 500,
                status="error",
                event = event,
                message=str(exc)
            )
            return JSONResponse(status_code=500, content={"details": event})
        