from flask import Flask, request, jsonify
import numpy as np
from src.mlProject.pipeline.prediction import PredictionPipeline
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)   # IMPORTANT for Vercel frontend

# Health check (optional but recommended)
@app.route("/", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "message": "Wine Quality API is running"
    })


# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = [
            float(data["fixed_acidity"]),
            float(data["volatile_acidity"]),
            float(data["citric_acid"]),
            float(data["residual_sugar"]),
            float(data["chlorides"]),
            float(data["free_sulfur_dioxide"]),
            float(data["total_sulfur_dioxide"]),
            float(data["density"]),
            float(data["pH"]),
            float(data["sulphates"]),
            float(data["alcohol"]),
        ]

        features = np.array(features).reshape(1, 11)

        model = PredictionPipeline()
        prediction = model.predict(features)

        return jsonify({
            "success": True,
            "prediction": int(prediction[0])
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)