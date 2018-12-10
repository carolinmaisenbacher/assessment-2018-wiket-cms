from app.authentification import blueprint
from flask import request, abort, jsonify, make_response, redirect
import html

# uses the blowfish cipher salt, (prevents rainbow tables)
import bcrypt
from app.authentification.sessions import login as login_user, logout as logout_user
from app.authentification.models import Owner
from app import db

@blueprint.route("/signup", methods=["POST"])
def create_user():
    if not request.json:
        abort(400)
    email = request.json['email']
    if not email:
        return make_response(jsonify({"error": "You have to provide a valid Email"}), 401)

    password = request.json['password']

    if not password:
        return make_response(jsonify({"error": "You have to provide a Password"}), 401)

    first_name = request.json['first_name']
    last_name = request.json['last_name']
    restaurant_id = request.json['restaurant_id']

    if not first_name or not last_name:
        return make_response(jsonify({"error": "You have to provide a First and a Lastname"}), 401)
   
    if Owner.query.filter(Owner.email==email).first():
        return make_response(jsonify({"error": "You already exist, please log in"}), 401)

    new_owner = Owner.create_owner(first_name=first_name, last_name=last_name, email=email, password=password, restaurant_id=restaurant_id)
 
    response = make_response("user created", 201)
    return login_user(new_owner, response)

@blueprint.route("/login", methods=["POST"])
def login():
    if not request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    password = request.json['password']
    email = request.json['email'] 

    owner = Owner.query.filter(Owner.email==email).first()
    if not owner:
        return make_response(jsonify({"error": "Username or password incorrect!"}), 401)

    if not owner.check_password(password):  
        return make_response(jsonify({"error": "Username or password incorrect"}), 401)

    response = redirect("/admin")
    login_user(owner, response)
    return response

