import logging
import json
from app.helpers.logLevels import ERRORLOGS,INFOLOGS,WARNINGLOGS
from app.helpers.context import request_id_ctx
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

logger = logging.getLogger(__name__)

def log_event(level, event, status, message, status_code=200, extra=None):
    log = {
        "event": event,
        "status": status,
        "status_code": status_code,
        "message": message,
        "service": "my-demo-app",
        "request_id": request_id_ctx.get(),
        "timestamp": datetime.utcnow().isoformat()
    }

    if extra:
        log.update(extra)

    log_json = json.dumps(log, separators=(",", ":"))

    if level == INFOLOGS:
        logger.info(log_json)
    if level == WARNINGLOGS:
        logger.warning(log_json)
    if level == ERRORLOGS:
        logger.error(log_json)