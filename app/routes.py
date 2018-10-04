# your routes live here
from app import app
from flask import request, abort
import bcrypt

users= []


@app.route("/")
def index():
    return "Hello"
    
    
@app.route("/login", methods=["POST"])
def create_user():
    if not request.json or not 'password' in request.json or not 'username' in request.json:
        abort(400)
    password = request.json['password']
    print(password)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print(password)

    user = None

     # check if user exists already
    for saved_user in users:
        if saved_user.username == request.json['username']:
            user = saved_user


    #if not create new user
    if user == None: 
        print("new User")
        user = User(request.json['username'], hashed)
        users.append(user)


    else:
        # if yes, compare passwords
        if bcrypt.checkpw(password.encode(), user.hashed_password):
            print("It Matches!")   

        else:  
            print("It Does not Match :(") 

    string_of_users =  ''
    for user in users:
        string_of_users += user.username

    return string_of_users


class User ():
    def __init__(self, username, hashed_password):
        self.username = username
        self.hashed_password = hashed_password

    def getHashedPassword():
        return self.hashed_password

    def getUsername():
        return self.username