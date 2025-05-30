from sqlalchemy import create_engine

import os


user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
name = os.getenv('DB_NAME')
port = os.getenv('DB_PORT')

DATABASE_URL = f"postgresql://{user}:{password}@localhost:{port}/{name}"
engine = create_engine(DATABASE_URL, echo=False, future=True)