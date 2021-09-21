import psycopg2
import os

# utils.environment swaps environment variables on import
from utils.config import CONFIG

POSTGRES_USER = CONFIG["development"]["database"]["pg_user"]
POSTGRES_PASS = CONFIG["development"]["database"]["pg_pass"]
POSTGRES_DATABASE = CONFIG["development"]["database"]["pg_db"]
POSTGRES_HOST = CONFIG["development"]["database"]["pg_host"]
POSTGRES_PORT = CONFIG["development"]["database"]["pg_port"]

def make_pg_pool() -> psycopg2.connection:
    return psycopg2.connect(
        database=POSTGRES_DATABASE,
        user=POSTGRES_USER,
        password=POSTGRES_PASS,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
    )