#!/bin/bash

# Check if bot-env already exists
if [ ! -d "bot-env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv bot-env
else
    echo "Virtual environment already exists." 
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source "bot-env/bin/activate"

echo "Virtual environment is ready."

echo "Installing required packages..."
python3 -m pip install -r requirements.txt

alias botup='python3 "$(pwd)/Bot/run.py"'

echo "Setup complete. Use 'botup' to run the bot"