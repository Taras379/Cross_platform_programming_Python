from mypackage.module1 import TransLate, LangDetect, CodeLang, LanguageList

def main():
    # Тестування функції TransLate
    text = "Hello, world!"
    src_lang = "en"
    dest_lang = "es"
    translated_text = TransLate(text, src_lang, dest_lang)
    print(f"Translated text from '{src_lang}' to '{dest_lang}': {translated_text}")

    # Тестування функції LangDetect
    text_to_detect = "Bonjour tout le monde!"
    detected_language = LangDetect(text_to_detect, set="lang")
    print(f"Detected language: {detected_language}")

    # Тестування функції CodeLang
    language_code = CodeLang("French")
    print(f"Language code for 'French': {language_code}")

    # Тестування функції LanguageList
    result = LanguageList(out="screen", text="Good morning")
    print(f"Language list output: {result}")

if __name__ == "__main__":
    main()
