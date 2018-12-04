from app.authentification import blueprint
from flask import request, abort, jsonify, make_response
from app.authentification.sessions import Sessions
import html

# uses the blowfish cipher salt, (prevents rainbow tables)
import bcrypt
from app.authentification.models import Owner
from app import db

users = []   
id_counter = 0
sessions = Sessions()

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

    if not first_name or not last_name:
        return make_response(jsonify({"error": "You have to provide a First and a Lastname"}), 401)
   
    if Owner.query.filter(Owner.email==email).first():
        return make_response(jsonify({"error": "You already exist, please log in"}), 401)

    new_owner = Owner.create_owner(first_name=first_name, last_name=last_name, email=email, password=password)

    response = make_response(jsonify({"userId": new_owner.id}), 201)
    sessionId = sessions.create(new_owner.id)
    response.set_cookie("sessionId", value = sessionId)
    return response

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

    response = make_response(jsonify({"userId" : owner.id}), 200) 
    sessionId = sessions.create(owner.id)
    response.set_cookie("sessionId", value = sessionId)
    return make_response(jsonify({"id" : owner.id}))


class User ():
    def __init__(self, email, password):
        self.id = self.generate_id()
        self.email = email
        self.hashed_password = ""
        self.set_password(password)
    
    def generate_id(self):
        global id_counter
        id_counter += 1
        return id_counter
        

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.hashed_password)

    def set_password(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    @classmethod
    def find(_cls, email):
        for user in users:
            if user.email == email:
                return user


