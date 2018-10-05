# your routes live here
from app.main import blueprint

@blueprint.route("/")
def index():
    return "Hello"
    
    
