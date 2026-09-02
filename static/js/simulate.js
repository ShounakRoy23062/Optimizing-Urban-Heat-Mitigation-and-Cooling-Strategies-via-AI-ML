async function executeSimulation() {

    const roofs = Number(
        document.getElementById("sliderCoolRoof")?.value || 0
    );

    const trees = Number(
        document.getElementById("sliderTreeCanopy")?.value || 0
    );

    const pavements = Number(
        document.getElementById("sliderPavements")?.value || 0
    );

    try {

        const result = await runSimulationAPI(
            roofs,
            trees,
            pavements
        );

        if (!result) {
            alert("Simulation failed.");
            return;
        }

        const tempDrop =
            document.getElementById("simTempDrop");

        const cost =
            document.getElementById("simCost");

        const population =
            document.getElementById("simPop");

        if (tempDrop)
            tempDrop.textContent =
                `${result.temperature_drop}°C`;

        if (cost)
            cost.textContent =
                `₹${result.cost.toLocaleString()}`;

        if (population)
            population.textContent =
                result.population.toLocaleString();

    } catch (error) {

        console.error(
            "Simulation Error:",
            error
        );

        alert(
            "Unable to run simulation."
        );
    }
}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const button =
            document.getElementById(
                "runSimBtn"
            );

        if (button) {

            button.addEventListener(
                "click",
                executeSimulation
            );

        }

    }
);