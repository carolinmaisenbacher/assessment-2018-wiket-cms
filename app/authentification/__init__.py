from flask import Blueprint

blueprint = Blueprint('authentification', __name__)

from app.authentification import routes