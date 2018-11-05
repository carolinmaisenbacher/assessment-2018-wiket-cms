from app.config import Config
import psycopg2
import sample_datasets

datasets = {"owner" : "sample_datasets/dataset_user.csv",
            "restaurant" : "sample_datasets/dataset_restaurant.csv",
}

def load_csv(table_name, file, connection):
    try:
        with open(file, 'r') as f:
            column_names = f.readline()

        with open(file, 'rb') as f:
            cursor = connection.cursor()
            comand = f'COPY {table_name}({column_names}) FROM STDIN WITH (FORMAT CSV, HEADER)'
            cursor.copy_expert(comand, f)
            connection.commit()
            print(f"{file} loaded!")
    except psycopg2.IntegrityError:
        print(f"{file} already existed")
        connection.rollback()


connection = psycopg2.connect(dbname=Config.DATABASE_NAME, host="localhost", port=5432, user=Config.DATABASE_USER, password=Config.DATABASE_SECRET)

for dataset in datasets:
    load_csv(dataset, datasets[dataset],connection=connection)

connection.close()
