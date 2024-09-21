import os

import openai
import pyperclip
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")


def translate_text(text, source_language="en", target_language="fr"):
    prompt = f"Translate the following text from {source_language} to {target_language}. Only output the translation and nothing else. Text to translate: {text}"

    # Correct API method for the new API
    response = openai.chat.completions.create(
        model="gpt-4o",  # Use the GPT-4 model
        messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": prompt},
        ],
    )

    # Accessing the message content correctly
    return response.choices[0].message.content.strip()


def get_clipboard_content():
    return pyperclip.paste()


def main():
    text = get_clipboard_content()
    if not text:
        print("Clipboard is empty. Please copy some text.")
        return

    translated_text = translate_text(text)
    print(translated_text)  # Only print the translated text


if __name__ == "__main__":
    main()
