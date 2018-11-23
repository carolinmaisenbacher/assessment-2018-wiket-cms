# your routes live here
from app.main import blueprint
from flask import request
from app.main.models import Restaurant
from flask import jsonify,render_template

import json

@blueprint.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method=='POST':
        restaurants = Restaurant.query.all()
        return str(restaurants)
    
    
@blueprint.route("/<id>", methods=["POST"])
def restaurant(id):
    if request.method=='POST':
        restaurant = Restaurant.query.get(id)
        return jsonify("Hello")