from sqlalchemy import text
from app.db import get_engine
from .base import HealthCheck

class DataBaseHealthCheck(HealthCheck):
    
    def check(self) -> bool:
        try:
            engine = get_engine()

            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            return True
        
        except Exception:
            return False
