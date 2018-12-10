from app.api import blueprint as bp
from app import db
from flask import jsonify, request, abort, make_response
from app.main.models import TextActive
from app.authentification.sessions import is_authorized

@bp.route('/texts/<int:id>', methods=['PUT'])
def update_texts(id):
    text = TextActive.query.filter(TextActive.text_id==id).first()
    if not request.json:
        abort(400)
    if not 'id' in request.json and type(request.json['id']) != unicode:
        abort(400)
    if not 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)

    if not 'text' in request.json and type(request.json['text']) is not unicode:
        abort(400)

    if not 'position' in request.json and type(request.json['position']) is not int:
        abort(400)
    
    data = request.json
    

    owner_information = is_authorized(request, text.restaurant_id)
    if owner_information == False:
        return make_response("You are not authorized to change this text, maybe try to log in.", 401)

    text.from_dict(data)
    db.session.commit()
    
    changed_text = text.to_dict()
    print(changed_text)
    return make_response(jsonify(changed_text), 201)