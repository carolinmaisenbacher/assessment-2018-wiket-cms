# your routes live here
from app.main import blueprint
from flask import request
from app.main.models import Restaurant
from flask import jsonify

@blueprint.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return jsonify("Hello")
    if request.method=='POST':
        restaurants = Restaurant.query.all()
        return jsonify(restaurants)
    
    
