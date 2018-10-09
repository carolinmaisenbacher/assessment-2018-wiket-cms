# your routes live here
from app.main import blueprint
from flask import jsonify

@blueprint.route("/")
def index():
    return jsonify("Hello")
    
    
