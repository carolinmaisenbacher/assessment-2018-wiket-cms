from app.api import blueprint as bp
from flask import jsonify, make_response
from app.main.models import Restaurant

@bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    return jsonify(Restaurant.query.get_or_404(id).to_dict())

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    return make_response(jsonify(Restaurant.collection_dict()),200)
