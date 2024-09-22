#!/usr/bin/env python3

import argparse
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
    # Argument parsing
    parser = argparse.ArgumentParser(description="Translate clipboard content.")
    parser.add_argument(
        "-src",
        "--source",
        type=str,
        default="en",
        help="Source language (default is 'en')",
    )
    parser.add_argument(
        "-tgt",
        "--target",
        type=str,
        default="fr",
        help="Target language (default is 'fr')",
    )
    args = parser.parse_args()

    # Fetch clipboard content
    text = get_clipboard_content()
    if not text:
        print("Clipboard is empty. Please copy some text.")
        return

    # Perform translation
    translated_text = translate_text(
        text, source_language=args.source, target_language=args.target
    )
    print(translated_text)


if __name__ == "__main__":
    main()
