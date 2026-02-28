let map = L.map('map').setView([9.96, 76.24], 8);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18
}).addTo(map);

const harbors = [
    {name: "Kochi Harbor", lat: 9.9667, lon: 76.2415},
    {name: "Alappuzha Harbor", lat: 9.4981, lon: 76.3388},
    {name: "Vizhinjam Harbor", lat: 8.4360, lon: 76.9800}
];

harbors.forEach(h => {
    L.marker([h.lat, h.lon]).addTo(map).bindPopup(h.name);
});

// Get user location
function getWeather() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
            const lat = pos.coords.latitude;
            const lon = pos.coords.longitude;
            fetch("/weather", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({lat, lon})
            })
            .then(res => res.json())
            .then(data => {
                const safety = data.safety;
                document.getElementById("safety").innerText = safety;
                document.getElementById("safety").style.color = safety;
            });
        });
    }
}

function sendSOS() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
            const lat = pos.coords.latitude;
            const lon = pos.coords.longitude;
            fetch("/sos", {
                method: "POST",
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({lat, lon, message: "Help! SOS"})
            })
            .then(res => res.json())
            .then(data => alert("SOS Sent!"));
        });
    }
}