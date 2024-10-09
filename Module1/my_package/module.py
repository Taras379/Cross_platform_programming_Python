import math

# Функція для перевірки належності точки до тора
def is_point_in_torus(x, y, r, R):
    distance = math.sqrt(x ** 2 + y ** 2)
    if r < distance < R:
        return True, distance
    return False, distance

# Функція для перекладу
def translate(text, language):
    translations = {
        'uk': {
            'coordinates': 'Координати точки А(x,y)',
            'first_radius': 'Радіус першого кола r',
            'second_radius': 'Радіус другого кола R',
            'distance': 'Відстань до точки A',
            'point_inside': 'Точка знаходиться всередині тора',
            'point_outside': 'Точка не знаходиться всередині тора'
        },
        'en': {
            'coordinates': 'Coordinates of point A(x,y)',
            'first_radius': 'Radius of the first circle r',
            'second_radius': 'Radius of the second circle R',
            'distance': 'Distance to point A',
            'point_inside': 'The point is inside the torus',
            'point_outside': 'The point is not inside the torus'
        }
    }

    return translations.get(language, translations['uk']).get(text, text)