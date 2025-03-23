from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

# Load the trained intrusion detection model
model_path = "rf_model.pkl"

# Check if model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found. Make sure the file is in the correct path.")

model = joblib.load(model_path)

# Initialize Flask app
app = Flask(__name__, template_folder="templates")

# Route to render the homepage
@app.route('/', methods=['GET'])
def home():
    """Render the index.html page."""
    return render_template('index.html')

# Route for threat prediction and scoring
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json.get('features', [])
        
        if not data:
            return jsonify({"error": "No feature data provided."}), 400
        
        data = np.array(data).reshape(1, -1)
        prediction = model.predict(data)
        
        # Define risk level based on prediction
        risk_score = "Low" if prediction[0] == 0 else "High"
        
        return jsonify({
            "prediction": int(prediction[0]),
            "risk_score": risk_score
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for dynamic firewall policy update
@app.route('/respond', methods=['POST'])
def respond():
    threat_type = request.json.get('threat_type', "")
    
    if threat_type == "DDoS":
        response = {"action": "Rate limiting applied"}
    elif threat_type == "Malware":
        response = {"action": "Device quarantined"}
    else:
        response = {"action": "Monitoring mode enabled"}
    
    return jsonify(response)

# Route for self-healing and rollback
@app.route('/recover', methods=['POST'])
def recover():
    device_id = request.json.get('device_id', "")
    
    if not device_id:
        return jsonify({"error": "Device ID not provided."}), 400
    
    # Simulated rollback mechanism
    rollback_status = f"Device {device_id} restored to previous safe state."
    
    return jsonify({
        "rollback_status": rollback_status
    })

# Health check route
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "API is running successfully."})

# Run Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
