from app.api import blueprint as bp
from flask import jsonify
from app.main.models import MenuParagraph, Dish, DishVariant

@bp.route('/menu/<int:restaurant_id>', methods=['PUT'])
def update_menu(restaurant_id):
    pass