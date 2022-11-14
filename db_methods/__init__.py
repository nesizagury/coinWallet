import os

from dotenv import load_dotenv

load_dotenv()
CONNECTION = f"postgres://{os.getenv('DB_USER', 'postgres')}:{os.getenv('DB_PASSWORD', 'postgres')}" \
             f"@{os.getenv('DB_HOST')}:" \
             f"{os.getenv('DB_PORT', '5432')}/{os.getenv('DB_NAME', 'postgres')}"