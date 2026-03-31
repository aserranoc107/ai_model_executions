import httpx
import logging
import json
import psycopg2
import app.repository as repo
from app.helpers.logEvents import log_event
from app.helpers.logLevels import INFOLOGS
from app.exceptions.errors import LogicServiceError, LLMServiceError

logger = logging.getLogger("AI Model executions")
OLLAMA_URL = "http://localhost:11434/api/generat"


def get_all_executions():
    try:
        result = repo.get_all_executions()
        log_event(INFOLOGS, "Service get executions", 0, "Process successfully executed")
        return result
    except psycopg2.OperationalError as ex:
        raise LogicServiceError((str(ex)))

def create_execution(data):
    try:
        result = repo.create_execution(data) 
        log_event(INFOLOGS, "Service create execution", 0, "Process successfully executed")
        return result  
    except psycopg2.OperationalError as ex:
        raise LogicServiceError((str(ex)))

def update_execution(execution_id, data):
    try:
        result = repo.update_execution(execution_id, data)
        log_event(INFOLOGS, "Service update execution", 0, "Process successfully executed")
        return result
    except psycopg2.OperationalError as ex:
        raise LogicServiceError((str(ex)))

async def run_model(prompt: str):
    try:
        log_event(INFOLOGS, "LLM execution started", 0, "Process starting")

        async with httpx.AsyncClient(timeout = 120) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": "llama3.2:1b",
                    "prompt": prompt,
                    "stream": False
                }
            )
        log_event(INFOLOGS, "LLM execution finished", 0, "Process successfully executed")
        return response.json()["response"]
    except (httpx.HTTPError, json.JSONDecodeError) as ex:
        print(f"type error like :{type(ex)} ")
        raise LLMServiceError((str(ex)))

def clean_response(text: str):
    return text.strip()

def save_result():
    return "Result saved to DB"




