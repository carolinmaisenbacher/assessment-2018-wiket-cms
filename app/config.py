import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DATABASE_USER = os.getenv("DATABASE_USER")
    DATABASE_SECRET = os.getenv("DATABASE_SECRET")
    DATABASE_HOST = os.getenv("DATABASE_HOST")
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_SECRET}@{DATABASE_HOST}/{DATABASE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    