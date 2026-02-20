from app.health.models import HealthCheckResult
from app.health.checks.database import DataBaseHealthCheck
from app.health.checks.config import ConfigHealthCheck

class HealthService:

    def __init__(self):
        self.checks = {
            "database": DataBaseHealthCheck(),
            "config": ConfigHealthCheck(),
        }

    def run_checks(self) -> HealthCheckResult:
        results = {}

        for name, check in self.checks.items():
            results[name] = "ok" if check.check() else "failed"

        overall_status = "ready" if all(
            status == "ok" for status in results.values()
        ) else "not_ready"

        return HealthCheckResult(
            status=overall_status,
            checks=results
        )
#collects all checks, executes them, combines them, and produces one clear response