from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from infrastructure.vault_client import VaultClient

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")

if DATABASE_URL is None:
    secret_path = os.getenv("VAULT_DB_PATH")
    secret_key = os.getenv("VAULT_DB_KEY", "DB_URL")
    if secret_path:
        try:
            client = VaultClient()
            DATABASE_URL = client.read_secret(secret_path, secret_key)
        except Exception:
            DATABASE_URL = None

if not DATABASE_URL:
    raise RuntimeError("Database URL not configured")

engine = create_engine(DATABASE_URL, echo=False, future=True)
