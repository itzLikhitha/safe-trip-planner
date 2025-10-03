from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

# 1️⃣ Default status route
@app.route("/")
def home():
    return jsonify({"message": "SafeTrip Backend is running!"})

# 2️⃣ Status check route
@app.route("/status")
def status():
    return jsonify({"status": "ok", "version": "1.0"})

# 3️⃣ Trip planner dummy route
@app.route("/trip")
def trip():
    return jsonify({
        "trip_id": 101,
        "location": "Hyderabad",
        "best_time": "6:00 AM - 9:00 AM",
        "comfort_index": 85
    })

# 4️⃣ Safety alerts dummy route
@app.route("/alerts")
def alerts():
    return jsonify({
        "uv_index": "High",
        "heat_warning": False,
        "rain_alert": True,
        "message": "Carry umbrella, possible showers."
    })

# 5️⃣ Health check route
@app.route("/health")
def health():
    return jsonify({"server": "healthy", "uptime": "running"})

if __name__ == "__main__":
    app.run(debug=True)
