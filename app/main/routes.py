# your routes live here
from app.main import blueprint
from flask import request
from app.main.models import Restaurant
from flask import jsonify,render_template, redirect, make_response, abort
from app.authentification.sessions import is_logged_in, login as login_user, logout as logout_user
from app.authentification.models import Owner

import json

@blueprint.route("/", methods=["GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
@blueprint.route("/admin", methods=["GET"])
def admin():
    if not is_logged_in(request):
        return redirect('/login')
    if request.method == 'GET':
        return render_template('cms.html') 

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method =='GET':
        return render_template('signup.html')
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    if not first_name or not last_name or not email or not password:
        abort(400)

    if Owner.query.filter(Owner.email==email).first():
        return make_response("You already exist, please log in", 401)
    
    new_owner = Owner.create_owner(first_name=first_name, last_name=last_name, email=email, password=password)
 
    response = redirect('/admin')
    return login_user(new_owner, response)

@blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html') 
    
    email = request.form.get("email")
    password = request.form.get("password")

    if not password or not email:
        abort(400)

    owner = Owner.query.filter(Owner.email==email).first()
    if not owner:
        return make_response(jsonify({"error": "Username or password incorrect!"}), 401)

    if not owner.check_password(password):  
        return make_response(jsonify({"error": "Username or password incorrect"}), 401)
    return login_user(user = owner, response = redirect("/admin"))
   
@blueprint.route("/logout", methods=["GET"])
def logout():
    sessionId = request.cookies["sessionId"]
    if not sessionId:
        abort(400)
    logout_user(sessionId)

    return redirect("/")

@blueprint.route("/signup-api", methods=["GET"])
def signup_api():
    return render_template('signup-api.html')

@blueprint.route("/login-api", methods=["GET"])
def login_api():
    return render_template('login-api.html') 
   