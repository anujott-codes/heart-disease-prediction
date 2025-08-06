#!/bin/bash

# Setup script for the Heart Disease Predictor

echo "Setting up Heart Disease Predictor..."

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Create Python virtual environment
echo "Creating Python virtual environment..."
python -m venv venv

# Activate virtual environment and install Python dependencies
echo "Installing Python dependencies..."
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install flask pandas numpy scikit-learn==1.6.1 joblib

# Create directories for model files
mkdir -p models

echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Copy your model files (log_reg.pkl, scaler.pkl, columns.pkl) to the project root"
echo "2. Start the Python service: python scripts/model_integration.py"
echo "3. In another terminal, start the Next.js app: npm run dev"
echo "4. Open http://localhost:3000 in your browser"
