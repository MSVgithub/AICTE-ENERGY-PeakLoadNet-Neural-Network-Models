from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load Linear Regression model
lr = joblib.load("linear_model.joblib")

@app.route("/")
def home():
    return "Linear Regression API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json.get("features")

        if data is None:
            return jsonify({"error": "No 'features' field provided"}), 400

        # Convert to numpy array and reshape properly
        X = np.array(data, dtype=float).reshape(1, -1)

        pred = lr.predict(X)[0]
        return jsonify({"prediction": float(pred)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
