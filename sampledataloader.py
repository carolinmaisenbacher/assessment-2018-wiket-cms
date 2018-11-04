from app.config import Config
from sqlalchemy.sql import text
import psycopg2

Config.SQLALCHEMY_DATABASE_URI
connection = psycopg2.connect(dbname=Config.DATABASE_NAME, host="localhost", port=5432, user=Config.DATABASE_USER, password=Config.DATABASE_SECRET)

datasets = []

try:
    with open('dataset_user.csv', 'rb') as f:
        cursor = connection.cursor()
        cmd = 'COPY owner(id,first_name,last_name,email,password_hash) FROM STDIN WITH (FORMAT CSV, HEADER)'
        cursor.copy_expert(cmd, f)
        connection.commit()
except ValueError e:
    print("ups")
    connection.close()

connection.close()

