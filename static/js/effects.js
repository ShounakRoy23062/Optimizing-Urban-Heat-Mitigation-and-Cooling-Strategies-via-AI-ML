const ALERTS = [
    "THERMO-ISRO ONLINE",
    "SATELLITE LINK ACTIVE",
    "HEAT THREAT DETECTED",
    "CAUSAL ENGINE READY",
    "OPTIMIZATION ENGINE READY"
];

function createAlertTicker() {

    const ticker =
        document.getElementById("systemTicker");

    if (!ticker) return;

    let index = 0;

    ticker.textContent = ALERTS[0];

    setInterval(() => {

        index = (index + 1) % ALERTS.length;

        ticker.textContent = ALERTS[index];

    }, 3000);
}

function pulseHeaders() {

    const headers =
        document.querySelectorAll("h1, h2");

    if (!headers.length) return;

    setInterval(() => {

        headers.forEach(header => {

            header.style.textShadow =
                "0 0 15px #ff5500";

            setTimeout(() => {

                header.style.textShadow =
                    "0 0 20px #00e5ff";

            }, 700);

        });

    }, 2000);
}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        createAlertTicker();
        pulseHeaders();

    }
);