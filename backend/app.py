from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "SafeTrip backend running!"})

@app.route("/predict", methods=["GET"])
def predict():
    # Get query parameters (dummy inputs)
    location = request.args.get("location", "Hyderabad")
    date = request.args.get("date", "2025-09-25")
    activity = request.args.get("activity", "hiking")

    # Dummy response (replace later with ML model output)
    response = {
        "location": location,
        "date": date,
        "activity": activity,
        "rain_probability": "30%",  # dummy value
        "comfort_index": 72         # dummy value
    }
    return jsonify(response)

@app.route("/safety", methods=["GET"])
def safety():
    return jsonify({
        "uv_index": 5,
        "flood_alert": False,
        "heat_alert": True
    })

@app.route("/weather", methods=["GET"])
def weather():
    return jsonify({
        "temperature": 28,
        "humidity": 70,
        "wind_speed": 12
    })

if __name__ == "__main__":
    app.run(debug=True)
