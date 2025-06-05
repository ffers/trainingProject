from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DB_URL')

DATABASE_URL = DATABASE_URL
engine = create_engine(DATABASE_URL, echo=False, future=True)