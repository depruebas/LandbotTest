from flask import Blueprint, request, jsonify
from app.controllers.topic import handle_topic_request

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/api/topic', methods=['POST'])
def topic_route():
    data = request.get_json()
    return handle_topic_request(data)
