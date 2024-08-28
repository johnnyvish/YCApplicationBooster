#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Create run_app.sh script
cat > run_app.sh << EOL
#!/bin/bash
source venv/bin/activate
streamlit run app.py
EOL

# Make run_app.sh executable
chmod +x run_app.sh

echo "Setup completed successfully!"
echo "To run the app, use the following command:"
echo "./run_app.sh"