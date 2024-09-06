import pandas as pd
from datetime import datetime
import os


# Функція для розрахунку віку
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Функція для категоризації віку
def categorize_age(age):
    if age < 18:
        return 'younger_18'
    elif 18 <= age <= 45:
        return '18-45'
    elif 46 <= age <= 70:
        return '45-70'
    else:
        return 'older_70'


# Функція для створення XLSX файлу
def create_xlsx_from_csv(csv_filename, xlsx_filename):
    try:
        df = pd.read_csv(csv_filename)

        required_columns = ["Прізвище", "Ім’я", "По батькові", "Дата народження"]
        if not all(col in df.columns for col in required_columns):
            raise ValueError("В CSV файлі відсутні деякі необхідні стовпці.")

        df['Дата народження'] = pd.to_datetime(df['Дата народження'], errors='coerce')
        df['Вік'] = df['Дата народження'].apply(lambda x: calculate_age(x) if pd.notnull(x) else None)

        age_categories = ['younger_18', '18-45', '45-70', 'older_70']
        categorized_dfs = {cat: df[df['Вік'].apply(lambda x: categorize_age(x) == cat)] for cat in age_categories}

        # Додати дані до всіх аркушів
        with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='all', index=False)

            # Запис даних за віковими категоріями
            for cat in age_categories:
                categorized_df = categorized_dfs[cat]
                categorized_df = categorized_df[['Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']]
                categorized_df.index += 1
                categorized_df.index.name = '№'
                categorized_df.to_excel(writer, sheet_name=cat, index=True)

        print("Ok")

    except FileNotFoundError:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
    except Exception as e:
        print(f"Повідомлення про неможливість створення XLSX файлу: {e}")

create_xlsx_from_csv("employees.csv", "employees_age_groups.xlsx")