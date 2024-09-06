from mypackage.module2 import TransLate, LangDetect, CodeLang, LanguageList

def main():
    # Тестування функції TransLate
    text = "Hello, world!"
    src_lang = "en"
    dest_lang = "fr"
    translated_text = TransLate(text, src_lang, dest_lang)
    print(f"Translated text from '{src_lang}' to '{dest_lang}': {translated_text}")

    # Тестування функції LangDetect
    text_to_detect = "Hola, ¿cómo estás?"
    detected_language = LangDetect(text_to_detect, set="all")
    print(f"Detected language and confidence: {detected_language}")

    # Тестування функції CodeLang
    language_code = CodeLang("es")
    print(f"Language name for code 'es': {language_code}")

    # Тестування функції LanguageList
    result = LanguageList(out="screen", text="Good evening")
    print(f"Language list output: {result}")

if __name__ == "__main__":
    main()