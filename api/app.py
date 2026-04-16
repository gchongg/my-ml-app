from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/predict")
def predict():
    result = requests.get("http://inference:5001/run")
    return jsonify(result.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)