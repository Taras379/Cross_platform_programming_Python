from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Для забезпечення стабільності результатів
DetectorFactory.seed = 0

# Функція повертає текст перекладений на задану мову, або повідомлення про помилку
def TransLate(text: str, src: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=src, target=dest)
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return f"Помилка: {e}"

# Функція визначає мову та коефіцієнт довіри для заданого тексту, або повертає повідомлення про помилку
def LangDetect(text: str, set: str = "all") -> str:
    try:
        lang = detect(text)
        # langdetect не надає коефіцієнт довіри, тому просто повертаємо мову
        if set == "lang":
            return lang
        elif set == "confidence":
            return "N/A"
        else:
            return f"Detected(lang={lang}, confidence=N/A)"
    except LangDetectException as e:
        return f"Помилка: {e}"

# Функція повертає код мови, або назву мови
def CodeLang(lang: str) -> str:
    lang = lang.lower()
    try:
        # Словник коду мов для deep_translator
        language_dict = {
            'af': 'afrikaans', 'sq': 'albanian', 'ar': 'arabic', 'hy': 'armenian',
            'ca': 'catalan', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
            'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
            'fi': 'finnish', 'fr': 'french', 'de': 'german', 'el': 'greek',
            'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'he': 'hebrew',
            'hi': 'hindi', 'hu': 'hungarian', 'is': 'icelandic', 'id': 'indonesian',
            'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
            'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'la': 'latin',
            'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian',
            'ml': 'malayalam', 'mn': 'mongolian', 'my': 'myanmar', 'ne': 'nepali',
            'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'pl': 'polish',
            'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian',
            'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
            'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak',
            'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
            'sw': 'swahili', 'sv': 'swedish', 'tl': 'tagalog', 'ta': 'tamil',
            'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian',
            'ur': 'urdu', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
            'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
        }
        lang = lang.lower()
        if lang in language_dict.values():
            return [code for code, name in language_dict.items() if name == lang][0]
        elif lang in language_dict:
            return language_dict[lang].capitalize()
        else:
            return "Помилка: Не знайдено відповідного коду або назви мови"
    except Exception as e:
        return f"Помилка: {e}"

# Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів, а також текст, перекладений на цю мову
def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        # Словник мов для deep_translator
        language_dict = {
            'af': 'afrikaans', 'sq': 'albanian', 'ar': 'arabic', 'hy': 'armenian',
            'ca': 'catalan', 'hr': 'croatian', 'cs': 'czech', 'da': 'danish',
            'nl': 'dutch', 'en': 'english', 'eo': 'esperanto', 'et': 'estonian',
            'fi': 'finnish', 'fr': 'french', 'de': 'german', 'el': 'greek',
            'gu': 'gujarati', 'ht': 'haitian creole', 'ha': 'hausa', 'he': 'hebrew',
            'hi': 'hindi', 'hu': 'hungarian', 'is': 'icelandic', 'id': 'indonesian',
            'it': 'italian', 'ja': 'japanese', 'jw': 'javanese', 'kn': 'kannada',
            'kk': 'kazakh', 'km': 'khmer', 'ko': 'korean', 'la': 'latin',
            'lv': 'latvian', 'lt': 'lithuanian', 'lb': 'luxembourgish', 'mk': 'macedonian',
            'ml': 'malayalam', 'mn': 'mongolian', 'my': 'myanmar', 'ne': 'nepali',
            'no': 'norwegian', 'or': 'odia', 'ps': 'pashto', 'pl': 'polish',
            'pt': 'portuguese', 'pa': 'punjabi', 'ro': 'romanian', 'ru': 'russian',
            'sm': 'samoan', 'gd': 'scots gaelic', 'sr': 'serbian', 'st': 'sesotho',
            'sn': 'shona', 'sd': 'sindhi', 'si': 'sinhala', 'sk': 'slovak',
            'sl': 'slovenian', 'so': 'somali', 'es': 'spanish', 'su': 'sundanese',
            'sw': 'swahili', 'sv': 'swedish', 'tl': 'tagalog', 'ta': 'tamil',
            'te': 'telugu', 'th': 'thai', 'tr': 'turkish', 'uk': 'ukrainian',
            'ur': 'urdu', 'vi': 'vietnamese', 'cy': 'welsh', 'xh': 'xhosa',
            'yi': 'yiddish', 'yo': 'yoruba', 'zu': 'zulu'
        }
        table = "N Language ISO-639 code Text\n"
        table += "-" * 50 + "\n"
        for i, (code, name) in enumerate(language_dict.items(), 1):
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
