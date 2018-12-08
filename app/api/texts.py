from app.api import blueprint as bp
from flask import jsonify, request, abort, make_response
from app.main.models import Text, TextActive

@bp.route('/texts/', methods=['PUT'])
def update_texts():
    if not request.json:
        abort(400)
    id = request.json.get("id")

    # text = [text for text in texts if text['id'] == text_id]
    if not 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)

    if not 'text' in request.json and type(request.json['text']) is not unicode:
        abort(400)

    if not 'position' in request.json and type(request.json['position']) is not int:
        abort(400)
    text = Text.query.get_or_404(id)
    return make_response(jsonify({"success": "Hallo"}), 201)