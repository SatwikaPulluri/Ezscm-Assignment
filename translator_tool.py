from googletrans import Translator

translator = Translator()

def translate_text(text, dest_lang="en"):
    try:
        result = translator.translate(text, dest=dest_lang)
        return result.text
    except Exception as e:
        return f"Translation error: {str(e)}"
