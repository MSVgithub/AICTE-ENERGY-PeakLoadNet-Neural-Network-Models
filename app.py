from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load both models
with open("linear_model.pkl", "rb") as f:
    linear = pickle.load(f)

with open("randomforest_model.pkl", "rb") as f:
    rf = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]

    features = np.array(data).reshape(1, -1)

    linear_pred = linear.predict(features)[0]
    rf_pred = rf.predict(features)[0]

    return jsonify({
        "linear_prediction": float(linear_pred),
        "random_forest_prediction": float(rf_pred)
    })

@app.route("/")
def home():
    return "Electricity Load Prediction API is Running!"

if __name__ == "__main__":
    app.run()
