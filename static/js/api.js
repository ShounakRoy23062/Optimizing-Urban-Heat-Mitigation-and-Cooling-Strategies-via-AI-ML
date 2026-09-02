const API_BASE = "/api";

/* ==========================
   THERMAL FORECAST
========================== */

async function getForecast() {
    try {

        const response = await fetch(
            `${API_BASE}/predict`
        );

        if (!response.ok)
            throw new Error(
                "Forecast Server Offline"
            );

        return await response.json();

    } catch (error) {

        console.error(
            "THERMAL PREDICTION FAILURE",
            error
        );

        return null;
    }
}

/* ==========================
   CAUSAL ANALYSIS
========================== */

async function getCausalDrivers() {

    try {

        const response = await fetch(
            `${API_BASE}/causal`
        );

        if (!response.ok)
            throw new Error(
                "Causal Engine Offline"
            );

        return await response.json();

    } catch (error) {

        console.error(
            "CAUSAL ENGINE FAILURE",
            error
        );

        return null;
    }
}

/* ==========================
   SIMULATION
========================== */

async function runSimulationAPI(
    roofs,
    trees,
    pavements
) {

    try {

        const response = await fetch(
            `${API_BASE}/simulate`,
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    cool_roofs: roofs,
                    tree_canopy: trees,
                    permeable: pavements
                })
            }
        );

        if (!response.ok)
            throw new Error(
                "Simulation Service Offline"
            );

        return await response.json();

    } catch (error) {

        console.error(
            "SIMULATION FAILURE",
            error
        );

        return null;
    }
}

/* ==========================
   OPTIMIZATION
========================== */

async function optimizeBudgetAPI() {

    try {

        const response = await fetch(
            `${API_BASE}/optimize`
        );

        if (!response.ok)
            throw new Error(
                "Optimization Engine Offline"
            );

        return await response.json();

    } catch (error) {

        console.error(
            "OPTIMIZER FAILURE",
            error
        );

        return null;
    }
}

/* ==========================
   HEALTH CHECK
========================== */

async function getSystemHealth() {

    try {

        const response = await fetch(
            `${API_BASE}/health`
        );

        if (!response.ok)
            throw new Error(
                "Health Check Failed"
            );

        return await response.json();

    } catch (error) {

        console.error(
            "SYSTEM HEALTH FAILURE",
            error
        );

        return null;
    }
}