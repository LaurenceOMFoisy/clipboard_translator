# Clipboard Translator (cbt)

Welcome to **Clipboard Translator (cbt)**! This tool allows you to translate text from your clipboard between languages using OpenAI's GPT models.

## Table of Contents
1. [What Does This Tool Do?](#what-does-this-tool-do)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Using the Shell Command `cbt`](#using-the-shell-command-cbt)
5. [Troubleshooting](#troubleshooting)
6. [Uninstallation](#uninstallation)
7. [License](#license)

---

## What Does This Tool Do?

Clipboard Translator takes text that you’ve copied to your clipboard and translates it from one language to another using OpenAI's GPT models. For example:
- Copy text in English.
- Run the `cbt` command to translate it into French.
- Get the translated result directly in your terminal!

---

## Prerequisites

Before using this tool, make sure you have:
1. **Python 3.8+**: You can download Python from [here](https://www.python.org/downloads/).
2. **Poetry**: This tool manages the project's dependencies. Follow the instructions below to install it.

---

## Installation

### Step 1: Install Python (if you don’t have it)

If you don’t already have Python installed:
1. Go to [python.org](https://www.python.org/downloads/).
2. Download the latest version (at least 3.8).
3. Follow the installation instructions on the website.

### Step 2: Install Poetry

#### For Linux/macOS:
1. Open your terminal.
2. Run the following command to install Poetry:

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Add Poetry to your system’s PATH (if necessary):

    ```bash
    export PATH="$HOME/.local/bin:$PATH"
    ```

### Step 3: Clone the Clipboard Translator Repository

1. Open your terminal or PowerShell.
2. Run:

    ```bash
    git clone https://github.com/yourusername/clipboard_translator.git
    cd clipboard_translator
    ```

### Step 4: Install the Project Dependencies with Poetry

Run the following command inside the `clipboard_translator` folder to install all the required dependencies:

```bash
poetry install
```

### Step 5: Get yourself an OpenAI API key

The installer will create a `.env` file in the project directory and prompt you to input it. You need to add your OpenAI API key to this file. You can also do this manually:

2. Open the `~/.env` file with any text editor (Notepad, nano, VSCode, etc.), and type `OPENAI_API_KEY=putyourapikeyhere` with your actual OpenAI API key. You can get an API key by signing up at [OpenAI](https://beta.openai.com/signup/).

---

## Using the Shell Command `cbt`

### Step 1: Run the Setup Script

You can run the provided `setup.sh` script, which will handle creating a `cbt` command you can run from anywhere:

```bash
./cbt.sh
```

### Step 2: Use the `cbt` Command

Now that the command is set up, you can use `cbt` directly in the terminal to translate clipboard content.

#### To translate from English to French:

```bash
cbt -src en -tgt fr
```

#### To translate from French to English:

```bash
cbt -src fr -tgt en
```

This command translates the content currently copied to your clipboard and prints the result in the terminal.

---

## Troubleshooting

### Problem: The `cbt` command doesn’t work.

1. **Check the `PATH`**: Make sure the script is installed in a folder that’s part of your system’s `$PATH`.
2. **Run the script directly**: If the command `cbt` doesn’t work, try running it directly by using:

    ```bash
    ~/.local/bin/cbt
    ```

### Problem: Python errors

1. **Check Python version**: Ensure you have Python 3.8+ installed.
2. **Reinstall dependencies**: Run `poetry install` again to reinstall all the necessary packages.

---

## Uninstallation

If you want to remove Clipboard Translator from your system:

1. Remove the cloned project folder and the `cbt` commands:

    ```bash
    rm -rf /path/to/clipboard_translator
    rm ~/.local/bin/cbt
    rm ~/.local/bin/cbt.py
    ```

2. Remove any lines you added to your `.bashrc` or `.zshrc` for `$PATH` if necessary.

---

## License

No license. Rip this shit as much as you want.
