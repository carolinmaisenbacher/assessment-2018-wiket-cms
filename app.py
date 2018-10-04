from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "http://localhost:8080"}})


@app.route("/")
def index():
    return jsonify({
        1: "Funghi",
        2: "Salami",
        3: "Margarita"
    })



if __name__ == '__main__':
    app.run()
