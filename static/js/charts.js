async function buildForecastChart() {

    const canvas =
        document.getElementById(
            "forecastChart"
        );

    if (!canvas) return;

    const forecast =
        await getForecast();

    if (!forecast) return;

    new Chart(canvas, {

        type: "line",

        data: {
            labels: [
                "0h",
                "6h",
                "12h",
                "18h",
                "24h",
                "36h",
                "48h"
            ],

            datasets: [{
                label: "Heat Threat",

                data:
                    forecast.forecast,

                borderColor:
                    "#ff5500",

                backgroundColor:
                    "rgba(255,85,0,.2)",

                fill: true,

                tension: 0.4
            }]
        },

        options: {
            responsive: true
        }
    });

}

async function buildCausalChart() {

    const canvas =
        document.getElementById(
            "causalBarChart"
        );

    if (!canvas) return;

    const result =
        await getCausalDrivers();

    if (!result) return;

    const labels =
        result.drivers.map(
            x => x.name
        );

    const values =
        result.drivers.map(
            x => x.impact * 100
        );

    new Chart(canvas, {

        type: "bar",

        data: {
            labels: labels,

            datasets: [{
                label:
                    "Heat Contribution (%)",

                data: values,

                backgroundColor:
                    "#ff5500"
            }]
        },

        options: {
            responsive: true
        }
    });

}

async function buildRadarChart() {

    const canvas =
        document.getElementById(
            "causalRadar"
        );

    if (!canvas) return;

    new Chart(canvas, {

        type: "radar",

        data: {

            labels: [
                "NDVI",
                "Traffic",
                "Buildings",
                "Population",
                "Albedo"
            ],

            datasets: [{
                label:
                    "Threat Drivers",

                data: [
                    90,
                    75,
                    85,
                    72,
                    61
                ],

                backgroundColor:
                    "rgba(0,229,255,.2)",

                borderColor:
                    "#00e5ff"
            }]
        },

        options: {
            responsive: true
        }
    });

}

window.addEventListener(
    "DOMContentLoaded",
    () => {

        buildForecastChart();
        buildCausalChart();
        buildRadarChart();

    }
);