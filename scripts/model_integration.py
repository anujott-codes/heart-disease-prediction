"""
Python script to integrate your joblib models with the Next.js API
This script shows how to create a Python service that the Next.js API can call
"""

import joblib
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import sys
import os

app = Flask(__name__)

# Load your models (make sure these files are in the same directory)
try:
    model = joblib.load("log_reg.pkl")
    scaler = joblib.load("scaler.pkl")
    expected_columns = joblib.load("columns.pkl")
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    sys.exit(1)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the raw input from the request
        raw_input = request.json
        
        # Create DataFrame from the input
        input_df = pd.DataFrame([raw_input])
        
        # Add missing columns with 0 values
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0
        
        # Reorder columns to match expected_columns
        input_df = input_df[expected_columns]
        
        # Scale the numerical columns
        cols_to_scale = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        input_df.loc[:, cols_to_scale] = scaler.transform(input_df.loc[:, cols_to_scale])
        
        # Make prediction
        prediction = model.predict(input_df)[0]
        
        return jsonify({
            'prediction': int(prediction),
            'message': 'Prediction completed successfully'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
