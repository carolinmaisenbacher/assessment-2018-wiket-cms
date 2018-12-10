# your routes live here
from app.main import blueprint
from flask import request
from app.main.models import Restaurant
from flask import jsonify,render_template, redirect, make_response, abort
from app.authentification.sessions import is_logged_in, login as login_user, logout as logout_user, get_user_information
from app.authentification.models import Owner

import json
@blueprint.route("/", methods=["GET"])
def overview():
    if request.method == 'GET':
        return render_template('frontpage.html')

@blueprint.route("/<int:id>", methods=["GET"])
def index(id):
    if request.method == 'GET':
        return render_template('index.html', restaurant_id=id)
    
@blueprint.route("/admin", methods=["GET"])
def admin():
    if not is_logged_in(request):
        return redirect('/login')
    if request.method == 'GET':
        user_info = get_user_information(request)
        Restaurant.query.get_or_404(user_info["restaurant_id"])
        id=user_info["restaurant_id"]
        template = f'cms.{id}.html'
        return render_template(template) 

@blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method =='GET':
        return render_template('signup.html')
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")
    restaurant_id = request.form.get("restaurant_id")

    if not first_name or not last_name or not email or not password or not restaurant_id:
        abort(400)

    if Owner.query.filter(Owner.email==email).first():
        return make_response("You already exist, please log in", 401)
    
    new_owner = Owner.create_owner(first_name=first_name, last_name=last_name, email=email, password=password, restaurant_id=restaurant_id)
 
    return redirect('/login')

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
   