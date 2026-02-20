from pydantic import BaseModel
from typing import Dict

#This class define how the Health Checks will respond
#Responds like:
    #{
        #"status: "ready"
        #"checks": {
                    #"database": "ok",
                    #"config": "ok"
        # }
    #}

class HealthCheckResult(BaseModel):
    status: str
    checks: Dict[str, str]