import boto3
import json
from sqlalchemy import create_engine

DB_HOST = "localhost"
DB_PORT = 5435
DB_NAME = "demo"
SECRET_NAME = "env/microservice/postgres-demo"
REGION = "us-east-1"

def get_secret():
    client = boto3.client("secretsmanager", region_name=REGION)
    response = client.get_secret_value(SecretId=SECRET_NAME)
    secret = json.loads(response["SecretString"])
    return secret

def get_engine():
    secret = get_secret()

    connection_string = (
        f"postgresql+psycopg2://{secret['username']}:"
        f"{secret['password']}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(connection_string, echo=False)
    return engine

