import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker('uk_UA')  # Використання української локалізації

def generate_birthdate():
    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

def generate_gender():
    return random.choices(["Чоловіча", "Жіноча"], [0.6, 0.4])[0]

def generate_job():
    return fake.job()

def generate_record(gender):
    if gender == "Чоловіча":
        name = fake.first_name_male()
        surname = fake.last_name_male()
        middle_name = fake.middle_name_male()
    else:
        name = fake.first_name_female()
        surname = fake.last_name_female()
        middle_name = fake.middle_name_female()

    return {
        "Прізвище": surname,
        "Ім’я": name,
        "По батькові": middle_name,
        "Стать": gender,
        "Дата народження": generate_birthdate(),
        "Посада": generate_job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address().replace("\n", ", "),
        "Телефон": fake.phone_number(),
        "Email": fake.email()
    }


# Збереження даних у CSV
def save_to_csv_pandas(filename, num_records):
    records = []

    male_count = int(num_records * 0.6)
    female_count = num_records - male_count

    for _ in range(male_count):
        records.append(generate_record("Чоловіча"))

    for _ in range(female_count):
        records.append(generate_record("Жіноча"))

    df = pd.DataFrame(records)

    df.to_csv(filename, index=False)

save_to_csv_pandas("employees.csv", 2000)
