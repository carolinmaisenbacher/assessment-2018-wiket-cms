
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_SECRET = os.getenv("DATABASE_SECRET")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
