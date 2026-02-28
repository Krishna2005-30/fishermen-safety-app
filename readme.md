# Fishermen Safety & Weather Alert App

## 🌊 Project Description
The **Fishermen Safety App** is designed to help fishermen stay safe at sea by providing real-time weather updates, safety alerts, GPS-based location tracking, nearby harbors, and fishing hotspots. It combines safety and efficiency to minimize accidents and maximize productive fishing trips.

---

## 💻 Tech Stack
- **Frontend:** HTML, CSS, JavaScript, Leaflet.js
- **Backend:** Python, Flask
- **Database:** SQLite
- **APIs:** OpenWeatherMap API
- **Tools:** VS Code, Git, GitHub

---

## ✨ Features
1. **Weather Alerts & Safety Indicator** – Real-time sea condition updates with safety levels (Green, Yellow, Red).  
2. **Nearest Safe Harbor** – Shows the closest harbor with distance and directions.  
3. **SOS / Emergency Button** – Sends instant alerts with GPS coordinates to family or authorities.  
4. **Fishing Hotspots** – Highlights nearby areas with abundant fish.  
5. **Offline Mode** – Cache data when network is unavailable.  
6. **Interactive Map** – Displays user location, harbors, and fishing hotspots with different markers.

---

## ⚙️ Installation Commands
Make sure Python and Git are installed:

```bash
# Clone repository
git clone https://github.com/your-username/fishermen-safety-app.git
cd fishermen-safety-app

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt 

#pic url
https://drive.google.com/file/d/1jqdV3WhdynJzZV-0DIVnWGO2rvTwDXFm/view?usp=drive_link

#Architecture Diagram

Description:

Frontend: HTML/CSS/JS + Leaflet.js map

Backend: Flask serving APIs

Database: SQLite stores harbors, fish hotspots, and safety tips

APIs: OpenWeatherMap for real-time weather

#API Documentation (Backend)
1️⃣ Weather API

Endpoint:

GET /weather/<latitude>/<longitude>

Description: Fetches real-time weather for the given GPS coordinates.

Parameters:

Parameter	Type	Description
latitude	float	Latitude of user location
longitude	float	Longitude of user location

Response Example:

{
  "temp": 26.0,
  "wind_kph": 15.5,
  "wind_knots": 8.4,
  "safety": "🟢 Calm – Ideal for fishing.",
  "storm_alert": false,
  "advice": "Good conditions for fishing."
}

Usage:
The frontend fetches this endpoint to show weather, safety status, and alerts.

2️⃣ Nearest Harbor API

Endpoint:

GET /nearest_harbor/<latitude>/<longitude>

Description: Returns the closest harbor from the user’s location.

Parameters:

Parameter	Type	Description
latitude	float	Latitude of user location
longitude	float	Longitude of user location

Response Example:

{
  "name": "Harbor A",
  "latitude": 9.9312,
  "longitude": 76.2673,
  "distance_km": 3.5,
  "direction": "NE"
}

Usage:
Shows nearest harbor info in the dashboard and safety card.

3️⃣ Optional: Fish Hotspots API

Endpoint:

GET /fish_hotspots

Description: Returns a list of all known fishing hotspots.

Response Example:

[
  {"name": "Fish Spot 1", "latitude": 9.9400, "longitude": 76.2500},
  {"name": "Fish Spot 2", "latitude": 10.8600, "longitude": 76.2800}
]

Usage:
Frontend marks these spots on the map and alerts the user when nearby.

#Team Members
Krishnaveni T C