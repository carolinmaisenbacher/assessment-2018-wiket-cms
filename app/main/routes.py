# your routes live here
from app.main import blueprint
from flask import request
from app.main.models import Restaurant
from flask import jsonify,render_template

import json

@blueprint.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
@blueprint.route("/admin", methods=["GET"])
def admin():
    if request.method == 'GET':
        return render_template('cms.html') 

@blueprint.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

@blueprint.route("/login", methods=["GET"])
def login():
    return render_template('login.html') 
   
@blueprint.route("/<id>", methods=["POST"])
def restaurant(id):
    if request.method=='POST':
        restaurant = Restaurant.query.get(id)
        return jsonify("Hello")