from sqlalchemy import text
from db import get_engine


engine = get_engine()

def get_all_executions():
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM ai_model_executions ORDER BY id DESC")
        )

        return [dict(row._mapping) for row in result]
    

def create_execution(data):
    query = text("""
                 INSERT INTO ai_model_executions
                 (model_name, input_tokens, output_tokens, execution_time_ms, cost_estimate, status, executed_by)
                 VALUES (:model_name, :input_tokens, :output_tokens, :execution_time_ms, :cost_estimate, :status, :executed_by)
                 RETURNING id""")
    
    with engine.begin() as conn:
        result = conn.execute(query, data)
        return result.scalar()

def update_execution(execution_id, data):
    query = text("""UPDATE ai_model_executions 
                 SET model_name=:model_name,
                    input_tokens=:input_tokens,
                    output_token:output_tokens, 
                    execution_time_ms=:execution_time_ms, 
                    cost_estimate=:cost_estimate, 
                    status=:status, 
                    executed_by:executed_by
                 """)
    data["id"] = execution_id

    with engine.begin() as conn:
        result = conn.execute(query, data)
        return result.rowcount 