import os
import json
from my_package.module import is_point_in_torus, translate

file_name = 'MyData'

# Перевірка, чи існує файл MyData
if os.path.exists(file_name):
    try:
        # Читання даних з файлу
        with open(file_name, 'r') as f:
            data = json.load(f)

        # Перевірка наявності коректних даних
        if 'x' in data and 'y' in data and 'r' in data and 'R' in data and 'language' in data:
            x = data['x']
            y = data['y']
            r = data['r']
            R = data['R']
            language = data['language']

            # Виведення даних
            print(translate('coordinates', language) + f": {x}, {y}")
            print(translate('first_radius', language) + f": {r}")
            print(translate('second_radius', language) + f": {R}")

            # Перевірка точки
            is_inside, distance = is_point_in_torus(x, y, r, R)
            print(translate('distance', language) + f": {round(distance, 2)}")
            if is_inside:
                print(translate('point_inside', language))
            else:
                print(translate('point_outside', language))

            # Якщо дані успішно зчитані та оброблені, програма завершується
            exit(0)

        else:
            raise ValueError('Некоректні дані')

    except (json.JSONDecodeError, ValueError):
        print('Помилка читання даних. Введіть нові дані!')

else:
    print('Файл не знайдено. Введіть дані!')

# Введення нових даних
x = float(input('Введіть координати точки А(x): '))
y = float(input('Введіть координати точки А(y): '))
r = float(input('Введіть радіус першого кола r: '))
R = float(input('Введіть радіус другого кола R: '))
language = input('Введіть мову інтерфейсу (uk/en): ').lower()

# Збереження даних у файл
data = {
    'x': x,
    'y': y,
    'r': r,
    'R': R,
    'language': language
}

with open(file_name, 'w') as f:
    json.dump(data, f)

print(f'Дані збережено в файл {file_name}!')
