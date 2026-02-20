import os
import json
import boto3
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

def get_secret():
    region = os.getenv("REGION")
    secret_name = os.getenv("SECRETS_NAME")

    client = boto3.client("secretsmanager", region_name=region)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])

    return secret


def get_engine():
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    secret = get_secret()

    connection_string = (
        f"postgresql+psycopg2://{secret['user_name']}:"
        f"{secret['password']}@{db_host}:{db_port}/{db_name}"
    )

    engine = create_engine(connection_string, echo=False)
    return engine







