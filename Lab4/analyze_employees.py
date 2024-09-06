import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Функція для зчитування CSV файлу
def read_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data, None
    except Exception as e:
        return None, f"Помилка при відкритті файлу: {e}"

# Функція для обчислення віку
def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except Exception as e:
        return None

# Функція для категоризації віку
def categorize_age(age):
    if age is None:
        return None
    elif age < 18:
        return 'younger_18'
    elif 18 <= age <= 45:
        return '18-45'
    elif 45 < age <= 70:
        return '45-70'
    else:
        return 'older_70'

def main():
    file_path = 'employees.csv'
    data, error = read_csv(file_path)

    if error:
        print(error)
        return
    else:
        print("Ок, файл успішно відкрито!")

    if 'Стать' not in data.columns or 'Дата народження' not in data.columns:
        print("Неправильний формат CSV файлу. Перевірте наявність колонок 'Стать' і 'Дата народження'.")
        return

    # Рахуємо кількість чоловіків і жінок
    gender_counts = data['Стать'].value_counts()
    print("\nКількість співробітників по статі:")
    print(f"Кількість чоловіків: {gender_counts.get('Чоловіча', 0)}")
    print(f"Кількість жінок: {gender_counts.get('Жіноча', 0)}")

    # Побудова діаграми для статі
    plt.figure(figsize=(10, 6))
    gender_counts.plot(kind='bar', color=['blue', 'pink'], edgecolor='black')
    plt.title('Кількість співробітників по статі')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=0)
    plt.grid(axis='y')
    plt.show()

    data['Вік'] = data['Дата народження'].apply(calculate_age)

    if data['Вік'].isnull().any():
        print("Помилка при обчисленні віку. Перевірте формат дати народження.")
        return

    # Рахуємо кількість співробітників в кожній віковій категорії
    age_categories = data['Вік'].apply(categorize_age).value_counts()
    print("\nКількість співробітників в кожній віковій категорії:")
    for category, count in age_categories.items():
        print(f"{category}: {count}")

    # Побудова діаграми для вікових категорій
    plt.figure(figsize=(10, 6))
    age_categories.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Кількість співробітників по вікових категоріях')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Рахуємо кількість співробітників кожної статі в кожній віковій категорії
    gender_age_distribution = data.groupby(['Стать', data['Вік'].apply(categorize_age)]).size().unstack().fillna(0)
    print("\nКількість співробітників кожної статі в кожній віковій категорії:")
    print(gender_age_distribution)

    # Побудова діаграм для статі в кожній віковій категорії
    gender_age_distribution.plot(kind='bar', figsize=(12, 8), edgecolor='black')
    plt.title('Кількість співробітників кожної статі по вікових категоріях')
    plt.xlabel('Стать')
    plt.ylabel('Кількість')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.legend(title='Вікова категорія')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
