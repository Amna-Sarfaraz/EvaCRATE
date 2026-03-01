"""
EvaCRATE — Local Flask Application
===================================
Loads your trained crop_model.pkl and serves the farmer UI.

Run:
    python app.py
Then open: http://localhost:5000
"""

import os
import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from datetime import datetime
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# ── Load trained model ─────────────────────────────────────────
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'crop_model.pkl')
model = None

def load_model():
    global model
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print(f"✅  Model loaded from: {MODEL_PATH}")
    except FileNotFoundError:
        print(f"⚠️   crop_model.pkl not found at {MODEL_PATH}")
        print("    Place your crop_model.pkl in the same folder as app.py")
        model = None

load_model()

# ── Crop multipliers (must match training) ─────────────────────
CROP_MULTIPLIERS = {
    'tomato': 1.3,
    'wheat':  0.7,
    'potato': 1.0,
    # extended crops — use 1.0 as default for unknown
    'rice':   0.9,
    'maize':  0.85,
    'onion':  0.8,
    'apple':  0.95,
    'banana': 1.2,
    'mango':  1.15,
    'pepper': 1.1,
}

def get_risk_level(days: float) -> str:
    if days <= 0.5:  return 'Red'
    if days <= 2.0:  return 'Brown'
    if days <= 5.0:  return 'Yellow'
    return 'Green'

def formula_fallback(temp, humidity, days_stored, crop_multiplier):
    """Fallback formula if model not loaded — same formula used in training."""
    d = (10 - 0.1 * temp - 0.05 * humidity - 0.2 * days_stored) * crop_multiplier
    return max(0.1, round(float(d), 2))

def simulate_sensor():
    """Generate realistic Pakistan summer sensor values."""
    hour = datetime.now().hour + datetime.now().minute / 60
    daily = math.sin((2 * math.pi / 24) * hour - math.pi / 2)
    temp = round(29 + 6 * daily + np.random.normal(0, 0.6), 1)
    hum  = round(max(35, min(90, 64 + 8 * (-daily) + np.random.normal(0, 1.5))), 1)
    return temp, hum


# ═══════════════════════════════════════════════
#  ROUTES
# ═══════════════════════════════════════════════

@app.route('/')
def index():
    temp, hum = simulate_sensor()
    return render_template('index.html',
                           temp=temp,
                           hum=hum,
                           model_loaded=(model is not None))

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        temperature    = float(data.get('temperature', 28))
        humidity       = float(data.get('humidity', 65))
        days_stored    = int(data.get('days_stored', 5))
        crop           = str(data.get('crop', 'tomato')).lower().strip()
    except (ValueError, TypeError) as e:
        return jsonify({'error': f'Invalid input: {e}'}), 400

    crop_multiplier = CROP_MULTIPLIERS.get(crop, 1.0)

    # ── Run model ──────────────────────────────────────────────
    if model is not None:
        try:
            X = np.array([[temperature, humidity, days_stored, crop_multiplier]])
            days_to_rot = float(model.predict(X)[0])
            days_to_rot = max(0.1, round(days_to_rot, 2))
            source = 'model'
        except Exception as e:
            days_to_rot = formula_fallback(temperature, humidity, days_stored, crop_multiplier)
            source = f'fallback (model error: {e})'
    else:
        days_to_rot = formula_fallback(temperature, humidity, days_stored, crop_multiplier)
        source = 'fallback (model not loaded)'

    risk_level = get_risk_level(days_to_rot)

    return jsonify({
        'days_to_rot':      days_to_rot,
        'risk_level':       risk_level,
        'crop_multiplier':  crop_multiplier,
        'temperature':      temperature,
        'humidity':         humidity,
        'days_stored':      days_stored,
        'crop':             crop,
        'source':           source,
        'timestamp':        datetime.now().strftime('%d %b %Y, %H:%M'),
    })


@app.route('/api/sensor', methods=['GET'])
def sensor():
    """Returns fresh simulated sensor values."""
    temp, hum = simulate_sensor()
    return jsonify({'temperature': temp, 'humidity': hum})


if __name__ == '__main__':
    print("\n" + "="*50)
    print("  EvaCRATE — Smart Crop Storage Monitor")
    print("="*50)
    print(f"  Model status : {'Loaded ✅' if model else 'Not found ⚠️'}")
    print(f"  Open browser : http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
