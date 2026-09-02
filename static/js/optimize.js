async function loadOptimization() {

    const table = document.getElementById("paretoTable");

    if (!table) return;

    try {

        const result = await optimizeBudgetAPI();

        if (!result) {
            table.innerHTML =
                "<p>Optimization service unavailable.</p>";
            return;
        }

        table.innerHTML = `
            <div class="strategy-card">

                <h3>Recommended Strategy</h3>

                <p>
                    Cool Roofs:
                    ${result.recommended_plan.cool_roofs}%
                </p>

                <p>
                    Tree Canopy:
                    ${result.recommended_plan.tree_canopy}%
                </p>

                <p>
                    Permeable Pavements:
                    ${result.recommended_plan.permeable}%
                </p>

                <p>
                    Cooling Impact:
                    ${result.cooling}°C
                </p>

                <p>
                    Budget:
                    ₹${result.budget.toLocaleString()}
                </p>

            </div>
        `;

    } catch (error) {

        console.error(
            "Optimization Load Failed",
            error
        );

        table.innerHTML =
            "<p>Failed to load optimization data.</p>";
    }
}

document.addEventListener(
    "DOMContentLoaded",
    loadOptimization
);