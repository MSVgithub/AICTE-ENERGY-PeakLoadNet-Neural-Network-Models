from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load models
with open("linear_model.pkl", "rb") as f:
    linear_model = pickle.load(f)

with open("randomforest_model.pkl", "rb") as f:
    rf_model = pickle.load(f)

@app.route("/")
def home():
    return "ML Models are running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    arr = np.array(data).reshape(1, -1)

    linear_pred = linear_model.predict(arr)[0]
    rf_pred = rf_model.predict(arr)[0]

    return jsonify({
        "linear_prediction": float(linear_pred),
        "rf_prediction": float(rf_pred)
    })

if __name__ == "__main__":
    app.run()
