import os
from app.health.checks.base import HealthCheck

class ConfigHealthCheck(HealthCheck):

    REQUIRED_VARS = [
        "DB_PORT",
        "DB_HOST",
        "DB_NAME",
        "REGION",
        "SECRETS_NAME"
    ]

    def check(self) -> bool:
        try:
            for var in self.REQUIRED_VARS:
                if not os.getenv(var):
                    return False
                return True
        except Exception:
            return False