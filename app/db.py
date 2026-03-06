import os
import boto3
from dotenv import load_dotenv
from sqlalchemy import create_engine, event
from sqlalchemy.pool import NullPool

load_dotenv()

region = os.getenv("REGION")
db_host = os.getenv("DB_HOST")
db_port = int(os.getenv("DB_PORT"))
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_SERVER_USER")

print(boto3.client("sts").get_caller_identity())

rds = boto3.client("rds", region_name=region)
engine = create_engine(
    f"postgresql+psycopg2://{db_user}@{db_host}:{db_port}/{db_name}",
    pool_pre_ping=True,
    poolclass= NullPool
)

@event.listens_for(engine, "do_connect")
def provide_token(dialect, conn_rec, cargs, cparams):
    token = rds.generate_db_auth_token(
        DBHostname = db_host,
        Port = db_port,
        DBUsername = db_user,
        Region = region
    )

    cparams["password"] = token
    cparams["sslmode"] = "require"







