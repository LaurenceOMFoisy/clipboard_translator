
#!/bin/bash

# Install dependencies using Poetry
echo "Installing dependencies with Poetry..."
poetry install --no-root

# Check if Poetry installation was successful
if [ $? -ne 0 ]; then
    echo "Poetry installation failed. Please ensure you have Poetry installed and configured properly."
    exit 1
fi

# Ensure ~/.local/bin exists, create it if it doesn't
if [ ! -d "$HOME/.local/bin" ]; then
    echo "Creating ~/.local/bin directory..."
    mkdir -p "$HOME/.local/bin"
fi

# Move the cbt.py script to ~/.local/bin for easy access
echo "Copying cbt.py to ~/.local/bin..."
cp cbt.py ~/.local/bin/cbt.py

# Get the full path to the Poetry virtual environment
VENV_PATH=$(poetry env info --path)

# Create a shell script to call the `cbt.py` through Poetry's virtual environment
cat <<EOL > ~/.local/bin/cbt
#!/bin/bash
# This script uses the Poetry environment to run cbt.py from anywhere
source $VENV_PATH/bin/activate
python ~/.local/bin/cbt.py "\$@"
deactivate
EOL

# Make the cbt command executable
chmod +x ~/.local/bin/cbt

# Add ~/.local/bin to the PATH if it is not already there
if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo "Adding ~/.local/bin to your PATH..."
    if [ -n "$ZSH_VERSION" ]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
        echo "Please restart your terminal or run 'source ~/.zshrc' to apply changes."
    elif [ -n "$BASH_VERSION" ]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        echo "Please restart your terminal or run 'source ~/.bashrc' to apply changes."
    fi
else
    echo "~/.local/bin is already in your PATH."
fi

# Check if the ~/.env file exists; if not, create it and prompt for OpenAI API Key
if [ ! -f "$HOME/.env" ]; then
    echo "Creating ~/.env file..."
    touch "$HOME/.env"
fi

# Check if the API key is already in the .env file
if grep -q "OPENAI_API_KEY=" "$HOME/.env"; then
    echo "OpenAI API key already exists in ~/.env."
else
    # Prompt the user to enter the OpenAI API key
    echo "Please enter your OpenAI API key:"
    read -r openai_key

    # Append the API key to the ~/.env file
    echo "Adding OpenAI API key to ~/.env..."
    echo "OPENAI_API_KEY=$openai_key" >> "$HOME/.env"
    echo "Your OpenAI API key has been added to ~/.env."
fi

echo "Setup complete! You can now use the 'cbt' command to translate text from your clipboard."

