from app.authentification import blueprint
from flask import request, abort, jsonify, make_response
from app.authentification.sessions import Sessions
import bcrypt

users = []
data = {'pageTitle': 'Blaue Tische',
        'titleColor': '#88ff44'}
id_counter = 0
sessions = Sessions()

@blueprint.route("/signup", methods=["POST"])
def create_user():
    if not request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    email = request.json['email']
    if not email:
        return make_response(jsonify({"error": "You have to provide a valid Email"}), 401)

    password = request.json['password']

    if not password:
        return make_response(jsonify({"error": "You have to provide a Password"}), 401)

    if User.find(email):
        return make_response(jsonify({"error": "You already exist, please log in"}), 401)

    new_user = User(email, password)
    users.append(new_user)


    response = make_response(jsonify({"userId": new_user.id}), 201)
    sessionId = sessions.create(new_user.id)
    response.set_cookie("sessionId", value = sessionId)

    return response

@blueprint.route("/login", methods=["POST"])
def login():
    if not request.json or not 'password' in request.json or not 'email' in request.json:
        abort(400)
    password = request.json['password']
    email = request.json['email']

    user = User.find(email)
    if not user:
        return make_response(jsonify({"error": "Username or passowrd incorrect!"}), 401)

    if not user.check_password(password):
        return make_response(jsonify({"error": "Username or password incorrect"}), 401)

    response = make_response(jsonify({"userId" : user.id}), 200)
    sessionId = sessions.create(user.id)
    response.set_cookie("sessionId", value = sessionId)
    return response

@blueprint.route("/content", methods=["GET", "POST"])
def handle_data():
    if request.method == 'POST':
        # global data
        data = request.json[userData]
        printf(data)
        #TBD: post data to database
    else:
        return data


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
