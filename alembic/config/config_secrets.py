

import os
from urllib.parse import quote_plus

user = os.environ["DB_USER"]
host = os.environ.get("DB_HOST", "localhost:5432")
db = os.environ["DB_NAME"]

raw_password = os.environ["DB_PASS"]

encoded_pass = quote_plus(raw_password)

db_url = f"postgresql+psycopg2://{user}:{encoded_pass}@{host}/{db}"