import os
from dotenv import load_dotenv
import boto3
import json
from sqlalchemy import create_engine

load_dotenv()

def get_engine():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    connection_string = (
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    )
    
    return create_engine(connection_string, echo=False)



