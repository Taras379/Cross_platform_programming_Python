import re
import string
import locale

# Функція для очищення слів від знаків пунктуації
def clean_word(word):
    return word.strip(string.punctuation)


# Функція для визначення мови слова
def detect_language(word):
    if any('а' <= char <= 'я' or 'А' <= char <= 'Я' for char in word):
        return 'ukrainian'
    else:
        return 'english'

# Функція для обробки і сортування слів
def process_words(words):
    cleaned_words = [clean_word(word) for word in words if word]

    # Видалення дублікатів і сортування
    unique_words = sorted(set(cleaned_words), key=lambda x: (x[0].islower(), x.lower()))

    return unique_words

def main():
    file_path = 'text.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()

            if not text:
                print("Файл порожній!")
                return

            # Виділення першого речення
            sentences = re.split(r'(?<=[.!?])\s+', text)
            first_sentence = sentences[0] if sentences else ""
            print("Перше речення:")
            print(first_sentence)

            # Розділення тексту на слова
            words = re.findall(r'\b\w+\b', text)

            sorted_words = process_words(words)

            ukrainian_words = [word for word in sorted_words if detect_language(word) == 'ukrainian']
            english_words = [word for word in sorted_words if detect_language(word) == 'english']

            # Налаштування для правильного сортування
            locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

            print("\nУкраїнські слова (в алфавітному порядку):")
            for word in sorted(ukrainian_words, key=lambda x: (x[0].islower(), locale.strxfrm(x))):
                print(word)

            print("\nАнглійські слова (в алфавітному порядку):")
            for word in sorted(english_words, key=lambda x: (x[0].islower(), locale.strxfrm(x))):
                print(word)

            print(f"\nЗагальна кількість слів: {len(words)}")

    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")

if __name__ == "__main__":
    main()
