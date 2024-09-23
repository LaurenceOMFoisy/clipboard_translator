#!/usr/bin/env python3

import os
import openai
import pyperclip
from dotenv import load_dotenv
import argparse
import subprocess
import signal

# Path to store the PID of the last Zenity window
ZENITY_PID_FILE = '/tmp/zenity_pid.txt'

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

def close_previous_zenity_window():
    """Close the previous Zenity window by killing its process using the PID."""
    if os.path.exists(ZENITY_PID_FILE):
        with open(ZENITY_PID_FILE, 'r') as f:
            try:
                previous_pid = int(f.read().strip())
                # Try to terminate the previous Zenity window
                os.kill(previous_pid, signal.SIGTERM)
            except (ValueError, ProcessLookupError):
                pass  # Ignore errors if process no longer exists

def show_popup(message):
    """Show the Zenity popup with the translated text in a non-editable, resizable window."""
    close_previous_zenity_window()

    # Run Zenity with info mode for displaying non-editable text
    zenity_process = subprocess.Popen([
        'zenity', '--info', '--title=Translation', '--width=400', '--height=300',
        '--ok-label=Close', '--text', message
    ])

    # Save the Zenity process ID to a file
    with open(ZENITY_PID_FILE, 'w') as f:
        f.write(str(zenity_process.pid))

def main():
    parser = argparse.ArgumentParser(description="Translate clipboard content or highlighted text.")
    parser.add_argument('-src', '--source', type=str, default='en', help="Source language (default is 'en')")
    parser.add_argument('-tgt', '--target', type=str, default='fr', help="Target language (default is 'fr')")
    args = parser.parse_args()

    text = get_clipboard_content()
    if not text:
        show_popup("No highlighted text or clipboard content found.")
        return

    translated_text = translate_text(text, source_language=args.source, target_language=args.target)
    show_popup(translated_text)

if __name__ == "__main__":
    main()
