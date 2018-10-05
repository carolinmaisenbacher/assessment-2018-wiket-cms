# your routes live here
from app import app
from flask import request, abort, jsonify, make_response
import bcrypt

users= []


@app.route("/")
def index():
    return "Hello"
    
    
@app.route("/signup", methods=["POST"])
def create_user():
    if not request.json or not 'password' in request.json or not 'username' in request.json:
        abort(400)
    username = request.json['username'].strip()
    if not username:
        make_response(jsonify({"error": "You have to provide a Username"}), 401)
    
    # check if user exists already
    # isn't that an easy way to find out as a hacker whether an email exists already
    for saved_user in users:
        if saved_user.username == username:
            return make_response(jsonify({"error": "You already exist, please log in"}), 401)

    #if not create new user
    password = request.json['password'].strip()
   
    if not password:
        return make_response(jsonify({"error": "You have to provide a Password"}), 401)
     
    new_user = User(username, password)
    print(new_user.username)
    print(new_user.hashed_password)
    users.append(new_user)

    string_of_users =  ''
    for user in users:
        string_of_users += user.username

    return make_response(jsonify({"userId": user.username, "all_users": string_of_users}))



@app.route("/login", methods=["POST"])
def signin():
    if not request.json or not 'password' in request.json or not 'username' in request.json:
        abort(400)
    password = request.json['password']

    user = None
     # check if user exists
    for saved_user in users:
        if saved_user.username == request.json['username']:
            user = saved_user

    if user == None:
        return make_response(jsonify({"error": "Username or passowrd incorrect!"}), 401)

    # check it correct password
    if user.check_password(password):
        return make_response(jsonify({"userId" : user.username}), 200) 

    else:  
        return make_response(jsonify({"error": "Username or password incorrect"}), 401)

class User ():
    def __init__(self, username, password):
        self.username = username
        self.hashed_password = ""
        self.set_password(password)

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.hashed_password)

    def set_password(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())