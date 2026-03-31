import psycopg2
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.db import engine
from app.helpers.logEvents import log_event
from app.helpers.logLevels import INFOLOGS
from app.exceptions.errors import DataServiceError

def get_all_executions():
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM ai_model_executions ORDER BY id DESC")
            )
            data = [dict(row._mapping) for row in result]

        log_event(INFOLOGS, "Service SQL get executions", 0, "Process successfully executed")
        return data
    except SQLAlchemyError as e:
        raise DataServiceError((str(e)))

def create_execution(data):
    try:
        query = text("""
            INSERT INTO ai_model_executions
            (model_name, input_tokens, output_tokens, execution_time_ms, cost_estimate, status, executed_by)
            VALUES (:model_name, :input_tokens, :output_tokens, :execution_time_ms, :cost_estimate, :status, :executed_by)
            RETURNING id
        """)

        with engine.begin() as conn:
            result = conn.execute(query, data)

        log_event(INFOLOGS, "create_execution", 200, "Execution record created")

        return result.scalar()

    except SQLAlchemyError as e:
        raise DataServiceError((str(e)))

def update_execution(execution_id, data):
    try:
        query = text("""
            UPDATE ai_model_executions 
            SET model_name=:model_name,
                input_tokens=:input_tokens,
                output_tokens=:output_tokens, 
                execution_time_ms=:execution_time_ms, 
                cost_estimate=:cost_estimate, 
                status=:status, 
                executed_by=:executed_by
            WHERE id = :id
        """)
        data["id"] = execution_id

        with engine.begin() as conn:
            result = conn.execute(query, data)
            log_event(INFOLOGS, "Service SQL update executions", 0, "Process successfully executed")
            return result.rowcount 
    
    except SQLAlchemyError as e:
        raise DataServiceError((str(e)))