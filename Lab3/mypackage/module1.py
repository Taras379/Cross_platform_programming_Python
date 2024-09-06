from googletrans import Translator, LANGUAGES

translator = Translator()

# Функція повертає текст перекладений на задану мову, або повідомлення про помилку
def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translation = translator.translate(text, src=src, dest=dest)
        return translation.text
    except Exception as e:
        return f"Помилка: {e}"

# Функція визначає мову та коефіцієнт довіри для заданого тексту, або повертає повідомлення про помилку
def LangDetect(text: str, set: str = "all") -> str:
    try:
        detection = translator.detect(text)
        if set == "lang":
            return detection.lang
        elif set == "confidence":
            return str(detection.confidence)
        else:
            return f"Detected(lang={detection.lang}, confidence={detection.confidence})"
    except Exception as e:
        return f"Помилка: {e}"

# Функція повертає код мови, або назву мови
def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    else:
        for code, name in LANGUAGES.items():
            if name.lower() == lang:
                return code
        return "Помилка: Не знайдено відповідного коду або назви мови"

# Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів, а також текст, перекладений на цю мову
def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        languages = sorted(LANGUAGES.items(), key=lambda x: x[1])
        table = "N Language ISO-639 code Text\n"
        table += "-" * 50 + "\n"
        for i, (code, name) in enumerate(languages, 1):
            translated_text = text if text is None else TransLate(text, 'auto', code)
            table += f"{i} {name.capitalize()} {code} {translated_text}\n"

        if out == "screen":
            print(table)
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as file:
                file.write(table)
        else:
            return "Помилка: Неправильний параметр 'out'."

        return "Ok"
    except Exception as e:
        return f"Помилка: {e}"
