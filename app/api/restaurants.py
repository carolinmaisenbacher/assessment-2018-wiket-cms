from app.api import blueprint as bp

@bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    pass

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    pass

@bp.route('/restaurants/<int:id>/menu', methods=['GET'])
def get_menu(id):
    pass

@bp.route('/restaurants/<int:id>/menu', methods=['PUT'])
def update_menu(id):
    pass