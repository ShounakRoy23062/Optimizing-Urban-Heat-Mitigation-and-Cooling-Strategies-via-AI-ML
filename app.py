from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

app = Flask(__name__)

# ==========================================
# PAGE ROUTES
# ==========================================

@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/causal")
def causal():
    return render_template("causal.html")


@app.route("/simulate")
def simulate():
    return render_template("simulate.html")


@app.route("/optimize")
def optimize():
    return render_template("optimize.html")


# ==========================================
# MAPBOX TOKEN API
# ==========================================

@app.route("/api/mapbox-token")
def get_mapbox_token():

    return jsonify({
        "token": os.getenv("MAPBOX_TOKEN")
    })


# ==========================================
# PREDICTION API
# ==========================================

@app.route("/api/predict")
def predict():

    return jsonify({
        "city": "Chennai",
        "current_temp": 45.7,
        "forecast": [46, 47, 48, 49, 48, 47, 46]
    })


# ==========================================
# CAUSAL ANALYSIS API
# ==========================================

@app.route("/api/causal")
def causal_analysis():

    return jsonify({
        "drivers": [
            {
                "name": "Building Density",
                "impact": 0.89
            },
            {
                "name": "Vegetation",
                "impact": 0.77
            },
            {
                "name": "Traffic",
                "impact": 0.63
            },
            {
                "name": "Population",
                "impact": 0.58
            }
        ]
    })


# ==========================================
# SIMULATION API
# ==========================================

@app.route("/api/simulate", methods=["POST"])
def run_simulation():

    try:

        payload = request.get_json() or {}

        roofs = float(payload.get("cool_roofs", 0))
        trees = float(payload.get("tree_canopy", 0))
        pavements = float(payload.get("permeable", 0))

        temperature_drop = (
            roofs * 0.012 +
            trees * 0.018 +
            pavements * 0.009
        )

        cost = (
            roofs * 150000 +
            trees * 220000 +
            pavements * 100000
        )

        population = (
            roofs * 700 +
            trees * 1100 +
            pavements * 450
        )

        return jsonify({
            "temperature_drop": round(temperature_drop, 2),
            "cost": int(cost),
            "population": int(population)
        })

    except Exception as error:

        return jsonify({
            "error": str(error)
        }), 400


# ==========================================
# OPTIMIZATION API
# ==========================================

@app.route("/api/optimize")
def optimize_budget():

    return jsonify({
        "recommended_plan": {
            "cool_roofs": 65,
            "tree_canopy": 82,
            "permeable": 40
        },
        "cooling": 3.4,
        "budget": 12500000
    })


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/api/health")
def health():

    return jsonify({
        "status": "online",
        "project": "THERMO-ISRO"
    })


# ==========================================
# START SERVER
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )