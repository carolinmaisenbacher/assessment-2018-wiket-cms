from app.api import blueprint as bp
from flask import jsonify
from app.main.models import Restaurant

@bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    return jsonify(Restaurant.query.get_or_404(id).to_dict())

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    return jsonify(Restaurant.collection_dict())

@bp.route('/restaurants/<int:id>/menu', methods=['GET'])
def get_menu(id):
    pass

@bp.route('/restaurants/<int:id>/menu', methods=['PUT'])
def update_menu(id):
    pass