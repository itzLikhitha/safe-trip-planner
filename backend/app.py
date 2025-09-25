from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return jsonify({"message": "SafeTrip backend running!"})

# Predict route with dummy inputs
@app.route("/predict", methods=["GET"])
def predict():
    location = request.args.get("location", "Hyderabad")   # default Hyderabad
    date = request.args.get("date", "2025-09-25")          # default date
    return jsonify({
        "location": location,
        "date": date,
        "rain_probability": "30%",   # dummy value
        "comfort_index": 72          # dummy value
    })

# Safety route with dummy alerts
@app.route("/safety", methods=["GET"])
def safety():
    activity = request.args.get("activity", "outdoor")     # extra input
    return jsonify({
        "activity": activity,
        "uv_index": 5,
        "flood_alert": False,
        "heat_alert": True
    })

# Weather route with dummy weather info
@app.route("/weather", methods=["GET"])
def weather():
    location = request.args.get("location", "Hyderabad")
    return jsonify({
        "location": location,
        "temperature": 28,
        "humidity": 70,
        "wind_speed": 12
    })

if __name__ == "__main__":
    app.run(debug=True)
