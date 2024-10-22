import psycopg2

def print_table_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name};")
    rows = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]

    print(f"\nTable: {table_name}")
    print(", ".join(colnames))
    for row in rows:
        print(row)

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="pharmacy_db", user="myuser", password="mypassword", host="localhost", port="5432"
)
cursor = conn.cursor()

# Виведення даних з усіх таблиць
tables = ['Medicines', 'Suppliers', 'Supplies']
for table in tables:
    print_table_data(table)

# Закриття з'єднання
cursor.close()
conn.close()
