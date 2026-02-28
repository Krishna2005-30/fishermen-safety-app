import requests

API_KEY = "291164fa5e4d4aa9acc174910262702"

# Example location: Kochi
location = "Kochi"

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("✅ API is working!")
    print("Location:", data["location"]["name"])
    print("Temperature:", data["current"]["temp_c"], "°C")
    print("Wind Speed:", data["current"]["wind_kph"], "km/h")
    print("Condition:", data["current"]["condition"]["text"])
else:
    print("❌ API not working")
    print("Status Code:", response.status_code)
    print(response.text)