from app.api import blueprint as bp
from flask import jsonify, request, abort
from app.main.models import Text, TextActive

@bp.route('/texts/<int:text_id>', methods=['PUT'])
def update_texts(text_id):
    text = Text.query.get_or_404(text_id)
    text = [text for text in texts if text['id'] == text_id]
    if not request.json or not "text" in request.json:
        abort(400)
    if "title" in request.json:
        return jsonify({"hello":"there"})
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'text' in request.json and type(request.json['text']) is not unicode:
        abort(400)
    if 'position' in request.json and type(request.json['position']) is not int:
        abort(400)
    return jsonify({"text":"there"})