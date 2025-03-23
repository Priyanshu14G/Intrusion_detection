from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize Flask app
app = Flask(__name__)

# Load the trained LSTM model
model = load_model('model.h5')

# Load the tokenizer
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Define max length of input sequence
MAX_SEQUENCE_LENGTH = 45


@app.route('/', methods=['GET'])
def home():
    """Render the index.html page."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get text from the JSON request
        data = request.json
        text = data.get('text')

        # Check if text is provided
        if not text:
            return jsonify({'error': 'No input text provided'}), 400

        # Tokenize and pad the input text
        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=MAX_SEQUENCE_LENGTH)

        # Make prediction
        prediction = model.predict(padded_sequence)[0][0]

        # Prepare response based on the prediction
        result = "Attack Detected" if prediction > 0.5 else "Normal Traffic"

        return jsonify({
            'prediction': result,
            'confidence': float(prediction)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
