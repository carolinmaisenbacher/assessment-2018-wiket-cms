from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route("/")
def index():
    return jsonify({
        1: "Funghi",
        2: "Salami",
        3: "Margarita"
    })

@app.route("/firstComponent")
def firstComponent():
    return jsonify({
        "marke": "Mercedes",
        "kraftstoff": "Diesel",
        "Leistung": "300 ps"
        # 1: "Mercedes",
        # 2: "Volvo",
        # 3: "Volkswagen"
    })

@app.route("/secondComponent")
def secondComponent():
    return jsonify({
        1: "Apple",
        2: "Google",
        3: "Linux"
    })

@app.route("/thirdComponent")
def thirdComponent():
    return jsonify({
        1: "Festool",
        2: "Makita",
        3: "Mafell"
    })




if __name__ == '__main__':
    app.run()
