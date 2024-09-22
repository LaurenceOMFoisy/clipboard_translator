#!/bin/bash

# Install dependencies using Poetry
echo "Installing dependencies with Poetry..."
poetry install --no-root

# Check if Poetry installation was successful
if [ $? -ne 0 ]; then
    echo "Poetry installation failed. Please ensure you have Poetry installed and configured properly."
    exit 1
fi

# Move the cbt.py script to ~/.local/bin for easy access
echo "Copying cbt.py to ~/.local/bin..."
cp cbt.py ~/.local/bin/cbt.py

# Create a shell script to call the `cbt.py` through Poetry
cat <<EOL > ~/.local/bin/cbt
#!/bin/bash
# This script uses the Poetry environment to run cbt.py
poetry run python ~/.local/bin/cbt.py "\$@"
EOL

# Make the cbt command executable
chmod +x ~/.local/bin/cbt

echo "Setup complete! You can now use the 'cbt' command to translate text from your clipboard."

