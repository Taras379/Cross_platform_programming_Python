import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="pharmacy_db", user="myuser", password="mypassword", host="localhost", port="5432"
)

# Створення таблиць
with conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Medicines (
        registration_number SERIAL PRIMARY KEY,
        name VARCHAR(100),
        manufacture_date DATE,
        shelf_life INTEGER,
        category VARCHAR(50),
        price NUMERIC(10, 2),
        prescription_required BOOLEAN
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Suppliers (
        supplier_code SERIAL PRIMARY KEY,
        supplier_name VARCHAR(100),
        address VARCHAR(255),
        phone_number VARCHAR(15),
        contact_person VARCHAR(100),
        location VARCHAR(50)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Supplies (
        supply_code SERIAL PRIMARY KEY,
        supply_date DATE,
        medicine_id INTEGER REFERENCES Medicines(registration_number),
        quantity INTEGER,
        supplier_id INTEGER REFERENCES Suppliers(supplier_code)
    );
    """)

    print("Tables created successfully.")

# ЗАПОВНЕННЯ ТАБЛИЦЬ ДАНИМИ
# Додавання ліків
with conn:
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO Medicines (name, manufacture_date, shelf_life, category, price, prescription_required)
    VALUES
    ('Ibuprofen', '2023-01-01', 365, 'Anti-inflammatory', 12.50, TRUE),
    ('Paracetamol', '2022-12-01', 730, 'Painkiller', 8.99, FALSE),
    ('Vitamin C', '2023-06-10', 1095, 'Vitamins', 5.99, FALSE),
    ('Aspirin', '2023-05-15', 730, 'Anti-inflammatory', 10.75, TRUE),
    ('Amoxicillin', '2023-03-22', 365, 'Antibiotic', 15.50, TRUE),
    ('Zinc', '2023-07-01', 1095, 'Vitamins', 7.80, FALSE),
    ('Codeine', '2023-09-01', 365, 'Painkiller', 20.00, TRUE),
    ('Diclofenac', '2023-04-20', 730, 'Anti-inflammatory', 9.99, TRUE),
    ('Ibuprom', '2023-02-14', 365, 'Painkiller', 11.00, TRUE),
    ('Panadol', '2023-01-10', 365, 'Painkiller', 10.00, FALSE),
    ('Vitrum', '2023-07-20', 1095, 'Vitamins', 12.30, FALSE),
    ('Magnesium B6', '2023-05-10', 1095, 'Vitamins', 13.50, FALSE),
    ('Azithromycin', '2023-08-01', 365, 'Antibiotic', 18.25, TRUE);
    """)

    # Додавання постачальників
    cursor.execute("""
    INSERT INTO Suppliers (supplier_name, address, phone_number, contact_person, location)
    VALUES
    ('Health Supply Co', '123 Main St', '380661234567', 'John Doe', 'Ukraine'),
    ('Global Pharma', '456 Global Ave', '380661234568', 'Jane Smith', 'Ukraine'),
    ('EuroPharm', '789 Europe St', '380661234569', 'Ivan Petrov', 'Other Country'),
    ('MedEx International', '1010 Med Way', '380661234570', 'Emily Davis', 'Other Country'),
    ('UkrPharma Ltd', '321 Industrial Blvd', '380661234571', 'Pavlo Koval', 'Ukraine');
    """)

    # Додавання поставок
    cursor.execute("""
    INSERT INTO Supplies (supply_date, medicine_id, quantity, supplier_id)
    VALUES
    ('2024-10-01', 1, 100, 1),
    ('2024-10-05', 2, 150, 2),
    ('2024-10-07', 3, 200, 3),
    ('2024-10-09', 4, 75, 4),
    ('2024-10-11', 5, 120, 5),
    ('2024-10-12', 6, 50, 1),
    ('2024-10-13', 7, 90, 2),
    ('2024-10-15', 8, 140, 3),
    ('2024-10-17', 9, 110, 4),
    ('2024-10-18', 10, 130, 5),
    ('2024-10-20', 11, 60, 1);
    """)

    print("Дані успішно створено!")

# Закриття з'єднання
conn.close()
