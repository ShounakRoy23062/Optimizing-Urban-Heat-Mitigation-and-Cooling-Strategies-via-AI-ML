const THREAT_ZONES = [
{
    zone: "Perambur",
    temp: 47.8,
    threat: "OMEGA",
    lat: 13.11,
    lng: 80.23
},
{
    zone: "Egmore",
    temp: 46.3,
    threat: "OMEGA",
    lat: 13.08,
    lng: 80.27
},
{
    zone: "Adyar",
    temp: 43.9,
    threat: "ALPHA",
    lat: 13.01,
    lng: 80.25
}
];

async function initializeMap() {

    if (!document.getElementById("map"))
        return;

    const response = await fetch("/api/mapbox-token");
    const data = await response.json();

    mapboxgl.accessToken = data.token;

    const map = new mapboxgl.Map({
        container: "map",
        style: "mapbox://styles/mapbox/dark-v11",
        center: [80.2707, 13.0827],
        zoom: 11
    });

    map.addControl(
        new mapboxgl.NavigationControl()
    );

    map.on("load", () => {

        THREAT_ZONES.forEach(zone => {

            const color =
                zone.temp > 46
                ? "#ff2200"
                : "#ffaa00";

            const popup =
                new mapboxgl.Popup()
                .setHTML(`
                    <h3>${zone.zone}</h3>
                    <p>${zone.temp}°C</p>
                    <p>${zone.threat}</p>
                `);

            new mapboxgl.Marker({
                color: color
            })
            .setLngLat([
                zone.lng,
                zone.lat
            ])
            .setPopup(popup)
            .addTo(map);

        });

    });
}

document.addEventListener(
    "DOMContentLoaded",
    initializeMap
);