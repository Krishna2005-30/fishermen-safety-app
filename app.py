from flask import Flask, render_template, jsonify
import sqlite3
import requests
import os
import math

app = Flask(__name__)

# --------------------
# Database functions
# --------------------
def get_harbors():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name, latitude, longitude FROM harbors")
    harbors = c.fetchall()
    conn.close()
    return harbors

def get_fish_hotspots():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT name, latitude, longitude FROM fish_hotspots")
    fish_spots = c.fetchall()
    conn.close()
    return fish_spots

# --------------------
# Landing Page
# --------------------
@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/map')
def home():
    harbors = get_harbors()
    fish_spots = get_fish_hotspots()
    return render_template('index.html', harbors=harbors, fish_spots=fish_spots)

# --------------------
# Weather API
# --------------------
@app.route('/weather/<float:lat>/<float:lon>')
def get_weather(lat, lon):
    API_KEY = "291164fa5e4d4aa9acc174910262702"  # 🔴 Replace with your key
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        temp = data["current"]["temp_c"]
        wind_kph = data["current"]["wind_kph"]
        condition_text = data["current"].get("condition", {}).get("text", "").lower()
        storm_alert = "storm" in condition_text
        wind_knots = wind_kph * 0.539957
    except Exception:
        return jsonify({
            "temp": None,
            "wind_kph": None,
            "wind_knots": None,
            "safety": "Data unavailable",
            "storm_alert": False,
            "advice": "Check internet/API key"
        })

    # Safety logic
    if storm_alert:
        safety = "Dangerous – Storm Alert"
        advice = "Return to nearest harbor!"
    elif wind_knots <= 10:
        safety = "Calm – Safe"
        advice = ""
    elif wind_knots <= 15:
        safety = "Breezy – Be alert"
        advice = ""
    elif wind_knots <= 20:
        safety = "Rough – High caution"
        advice = "Consider nearby harbor!"
    else:
        safety = "Dangerous – Do NOT go"
        advice = "Return to nearest harbor!"

    return jsonify({
        "temp": temp,
        "wind_kph": wind_kph,
        "wind_knots": round(wind_knots, 2),
        "safety": safety,
        "storm_alert": storm_alert,
        "advice": advice
    })

# --------------------
# Nearest Harbor API
# --------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def get_direction(d_lat, d_lon):
    lat_dir = "North" if d_lat > 0 else "South"
    lon_dir = "East" if d_lon > 0 else "West"
    return f"{lat_dir}-{lon_dir}"

@app.route('/nearest_harbor/<float:lat>/<float:lon>')
def nearest_harbor(lat, lon):
    harbors = get_harbors()
    nearest = None
    min_dist = float('inf')
    for h in harbors:
        dist = haversine(lat, lon, h[1], h[2])
        if dist < min_dist:
            min_dist = dist
            nearest = h
    d_lat = nearest[1] - lat
    d_lon = nearest[2] - lon
    direction = get_direction(d_lat, d_lon)
    return jsonify({
        "name": nearest[0],
        "distance_km": round(min_dist, 2),
        "direction": direction
    })

# --------------------
# Run app
# --------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)