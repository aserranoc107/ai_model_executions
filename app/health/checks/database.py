from sqlalchemy import text
from app.db import engine
from .base import HealthCheck

class DataBaseHealthCheck(HealthCheck):
    
    def check(self) -> bool:
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            return True
        
        except Exception:
            return False
