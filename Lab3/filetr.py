import os
import json
import re
from mypackage.module1 import TransLate, LangDetect
from langdetect import detect, DetectorFactory

# Для фіксації результатів детекції
DetectorFactory.seed = 0

def read_config(file_path):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except Exception as e:
        return f"Error reading config file: {e}"

def analyze_text(text):
    # Розрахунок кількості символів, слів і речень
    num_chars = len(text)
    num_words = len(re.findall(r'\w+', text))
    num_sentences = len(re.findall(r'[.!?]', text)) + text.count('\n')

    return num_chars, num_words, num_sentences


def main():
    config = read_config('config.json')
    if isinstance(config, str):  # Якщо повернено повідомлення про помилку
        print(config)
        return

    text_file = config.get('text_file')
    target_language = config.get('target_language')
    output_mode = config.get('output_mode')
    char_limit = config.get('char_limit')
    word_limit = config.get('word_limit')
    sentence_limit = config.get('sentence_limit')

    if not os.path.isfile(text_file):
        print(f"File {text_file} not found.")
        return

    try:
        with open(text_file, 'r') as file:
            text = file.read()

        num_chars, num_words, num_sentences = analyze_text(text)

        print(f"File name: {text_file}")
        print(f"File size: {os.path.getsize(text_file)} bytes")
        print(f"Number of characters: {num_chars}")
        print(f"Number of words: {num_words}")
        print(f"Number of sentences: {num_sentences}")

        lang = detect(text)
        print(f"Detected language: {lang}")

        # Зчитування тексту до виконання умов
        if (num_chars > char_limit or num_words > word_limit or num_sentences > sentence_limit):
            text = text[:char_limit]

        translated_text = TransLate(text, lang, target_language)

        # Вивід результату
        if output_mode == 'screen':
            print(f"Translated text into '{target_language}':")
            print(translated_text)
        elif output_mode == 'file':
            output_file = f"{os.path.splitext(text_file)[0]}_{target_language}.txt"
            try:
                with open(output_file, 'w') as file:
                    file.write(translated_text)
                print("Ok")
            except Exception as e:
                print(f"Error writing to file: {e}")
        else:
            print("Invalid output mode specified.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
