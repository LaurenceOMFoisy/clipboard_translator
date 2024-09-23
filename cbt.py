#!/usr/bin/env python3

import os
import openai
import pyperclip
from dotenv import load_dotenv
import argparse
import subprocess

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, source_language="en", target_language="fr"):
    prompt = f"Translate the following text from {source_language} to {target_language}. Only output the translation and nothing else. Text to translate: {text}"

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a translator."},
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()

def get_clipboard_content():
    return pyperclip.paste()

def show_popup(message):
    # Use Yad to show a popup window with the translated message
    subprocess.run(['yad', '--text', message, '--button=OK', '--center'])

def main():
    parser = argparse.ArgumentParser(description="Translate clipboard content.")
    parser.add_argument('-src', '--source', type=str, default='en', help="Source language (default is 'en')")
    parser.add_argument('-tgt', '--target', type=str, default='fr', help="Target language (default is 'fr')")
    args = parser.parse_args()

    text = get_clipboard_content()
    if not text:
        show_popup("Clipboard is empty. Please copy some text.")
        return

    translated_text = translate_text(text, source_language=args.source, target_language=args.target)
    show_popup(translated_text)  # Show the translated text in a popup window

if __name__ == "__main__":
    main()
