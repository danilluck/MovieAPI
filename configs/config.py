import os

from dotenv import load_dotenv

load_dotenv("configs/.env")

db_config = os.environ.get('DB_CONFIG')
print(111, db_config)
