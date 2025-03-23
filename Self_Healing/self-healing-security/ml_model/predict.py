# D:\priyanshu backup\CPP\Deep_Learning\Intrusion_detection\self-healing-security\ml_model\predict.py

import joblib
import os

# Correct model path
model_path = r"D:\priyanshu backup\CPP\Deep_Learning\Intrusion_detection\self-healing-security\ml_model\ton-iot_model.sav"

# Check if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Error: Model file not found at '{model_path}'")

# Load the model
model = joblib.load(model_path)

def classify_traffic(features):
    """
    Classify network traffic and return threat level.
    Args:
        features (list or numpy array): List of 44 features representing the traffic data.
    Returns:
        str: "Threat Detected" if malicious traffic, else "Normal Traffic"
    """
    # Check if the feature length is correct
    if len(features) != 44:
        raise ValueError(f"Incorrect number of features. Expected 44, but got {len(features)}")

    # Make prediction
    prediction = model.predict([features])
    
    # Return the result
    return "Threat Detected" if prediction[0] == 1 else "Normal Traffic"
