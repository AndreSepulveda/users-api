import os

POSTGRES_URL: str = os.getenv('POSTGRES_URL', 'localhost:8083')
POSTGRES_USER: str = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASS: str = os.getenv('POSTGRES_PASS', 'password')
POSTGRES_DATABASE_NAME: str = os.getenv('POSTGRES_DATABASE_NAME', 'postgres')
