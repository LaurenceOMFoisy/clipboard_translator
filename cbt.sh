#!/bin/bash

# Install required Python packages if not already installed
echo "Installing required Python packages..."
pip install -r requirements.txt

# Move the cbt.py script to ~/.local/bin/ and rename it to cbt for easy access
echo "Setting up the clipboard translator..."
mkdir -p ~/.local/bin
cp cbt.py ~/.local/bin/cbt

# Make it executable
chmod +x ~/.local/bin/cbt

# Add ~/.local/bin to the user's PATH if not already in it
if ! echo "$PATH" | grep -q "~/.local/bin"; then
    echo "export PATH=\$PATH:~/.local/bin" >> ~/.bashrc
    echo "Added ~/.local/bin to your PATH. Please restart your terminal or run 'source ~/.bashrc' to apply changes."
fi

echo "Setup complete! You can now use the 'cbt' command to translate text from your clipboard."
