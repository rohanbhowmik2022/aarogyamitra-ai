from transformers import pipeline

def translate_text(text, source_lang="en", target_lang="hi"):
    """
    Translate text from the source language to the target language.
    :param text: The input text to translate.
    :param source_lang: Source language code (e.g., 'en' for English).
    :param target_lang: Target language code (e.g., 'hi' for Hindi).
    :return: Translated text.
    """
    try:
        model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
        translator = pipeline("translation", model=model_name)
        translation = translator(text, max_length=400)
        return translation[0]['translation_text']
    except Exception as e:
        return f"Error during translation: {e}"

if __name__ == "__main__":
    print("Enter the text to translate (press Enter twice to finish):")
    input_text = ""
    while True:
        line = input()
        if line.strip() == "":
            break
        input_text += line + " "
    
    if input_text.strip():
        print("\nTranslating the input text...\n")
        translated_text = translate_text(input_text.strip(), source_lang="en", target_lang="hi")
        print("Translated Text:")
        print(translated_text)
    else:
        print("No input text provided.")