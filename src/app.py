from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

# Just mock data for now until we create a database
incomes = [
    {
        "description": "Salary",
        "amount": 3000
    }
]


@app.route("/")
def get_mainpage():
    return render_template("index.html", incomes=incomes)


@app.route("/incomes", methods=["GET"])
def get_income():
    return jsonify(incomes)


@app.route("/incomes", methods=["POST"])
def add_income():
    incomes.append(request.get_json())
    return "Success", 200


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "0.0.0.0"),
        port=os.environ.get("PORT", 5000),
        debug=os.environ.get("DEBUG", False)
    )
