from app.authentification import blueprint
from flask import request, abort, jsonify, make_response
import bcrypt

users = []   


@blueprint.route("/signup", methods=["POST"])
def create_user():
    if not request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    email = request.json['email']
    if not email:
        return make_response(jsonify({"error": "You have to provide a valid Email"}), 401)
    
    # check if user exists already
    # isn't that an easy way to find out as a hacker whether an email exists already
    if User.find(email):
        return make_response(jsonify({"error": "You already exist, please log in"}), 401)

    #if not create new user
    password = request.json['password']
   
    if not password:
        return make_response(jsonify({"error": "You have to provide a Password"}), 401)
     
    new_user = User(email, password)
    users.append(new_user)

    return make_response(jsonify({"userId": new_user.email}), 201)



@blueprint.route("/login", methods=["POST"])
def login():
    if not request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    password = request.json['password']

    user = None
     # check if user exists
    for saved_user in users:
        if saved_user.email == request.json['email']:
            user = saved_user

    if user == None:
        return make_response(jsonify({"error": "Username or passowrd incorrect!"}), 401)

    # check it correct password
    if user.check_password(password):
        return make_response(jsonify({"userId" : user.email}), 200) 

    else:  
        return make_response(jsonify({"error": "Username or password incorrect"}), 401)

class User ():
    def __init__(self, email, password):
        self.email = email
        self.hashed_password = ""
        self.set_password(password)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.hashed_password)

    def set_password(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    @classmethod
    def find(_cls, email):
        for user in users:
            if user.email == email:
                return user



