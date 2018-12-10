from app.config import Config
import psycopg2
import sample_datasets

standby = { 
}

datasets = {
             "owner" : "sample_datasets/dataset_owner.csv",
"restaurant" : "sample_datasets/dataset_restaurant.csv",
"text" : "sample_datasets/dataset_text.csv",
"text_active" : "sample_datasets/dataset_text_active.csv",
"menuparagraph" : "sample_datasets/dataset_menuparagraph.csv",
            "dish" : "sample_datasets/dataset_dish.csv",
            "dish_variant" : "sample_datasets/dataset_dish_variant.csv"
}

def load_csv(table_name, file, connection): 
    try:
        with open(file, 'r') as f:
            column_names = f.readline()

        with open(file, 'rb') as f:
            cursor = connection.cursor()
            command = f'COPY {table_name}({column_names}) FROM STDIN WITH (FORMAT CSV, HEADER)'
            cursor.copy_expert(command, f)
            connection.commit()
            print(f"{file} loaded!")
    except psycopg2.IntegrityError:
        print(f"{file} already existed")
        connection.rollback()


connection = psycopg2.connect(dbname=Config.DATABASE_NAME, host="localhost", port=5432, user=Config.DATABASE_USER, password=Config.DATABASE_SECRET)

for dataset in datasets:
    load_csv(dataset, datasets[dataset],connection=connection)

connection.close()
