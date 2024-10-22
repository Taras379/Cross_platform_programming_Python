import psycopg2

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="pharmacy_db", user="myuser", password="mypassword", host="localhost", port="5432"
)
cursor = conn.cursor()

# 1. Відобразити всі ліки, які відпускаються за рецептом лікаря
cursor.execute("""
SELECT * FROM Medicines WHERE prescription_required = TRUE ORDER BY name;
""")
prescription_medicines = cursor.fetchall()
print("Ліки, які потребують рецепта:")
for row in prescription_medicines:
    print(row)

# 2. Відобразити всі ліки за обраною групою
category = 'Vitamins'  # змініть за потреби
cursor.execute("""
SELECT * FROM Medicines WHERE category = %s;
""", (category,))
medicines_by_category = cursor.fetchall()
print(f"\nЛіки в категорії '{category}':")
for row in medicines_by_category:
    print(row)

# 3. Порахувати вартість, кожної поставки
cursor.execute("""
SELECT supply_code, (quantity * (SELECT price FROM Medicines WHERE registration_number = Supplies.medicine_id)) AS total_cost
FROM Supplies;
""")
supply_costs = cursor.fetchall()
print("\nЗагальні витрати на кожну поставку:")
for row in supply_costs:
    print(row)

# 4. Порахувати загальну суму грошей, яку сплатила аптека кожному постачальнику
cursor.execute("""
SELECT Suppliers.supplier_name, SUM(quantity * (SELECT price FROM Medicines WHERE registration_number = Supplies.medicine_id)) AS total_spent
FROM Supplies
JOIN Suppliers ON Supplies.supplier_id = Suppliers.supplier_code
GROUP BY Suppliers.supplier_name;
""")
total_spent = cursor.fetchall()
print("\nЗагальна сума витрат для кожного постачальника:")
for row in total_spent:
    print(row)

# 5. Порахувати кількість поставок для кожної групи ліків від вітчизняних та закордонних постачальників
cursor.execute("""
SELECT Medicines.category, Suppliers.location, COUNT(Supplies.supply_code) AS supply_count
FROM Supplies
JOIN Medicines ON Supplies.medicine_id = Medicines.registration_number
JOIN Suppliers ON Supplies.supplier_id = Suppliers.supplier_code
GROUP BY Medicines.category, Suppliers.location;
""")
supply_count = cursor.fetchall()
print("\nКількість поставок для кожної категорії за місцем розташування постачальника:")
for row in supply_count:
    print(row)

# 6. Порахувати останню дату придатності для кожної ліки
cursor.execute("""
SELECT name, manufacture_date + INTERVAL '1 day' * shelf_life AS expiry_date
FROM Medicines;
""")
expiry_dates = cursor.fetchall()
print("\nТерміни придатності кожного препарату:")
for row in expiry_dates:
    print(row)

# Закриття з'єднання
conn.commit()
cursor.close()
conn.close()
