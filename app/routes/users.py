from flask import Blueprint, request, jsonify
from app.services.user_services import create_user, authenticate_user

user_blueprint = Blueprint('users',__name__)

@user_blueprint.route('/signup', methods=['POST'])
def signup():
    data= request.get_json()
    result = create_user(data)
    return jsonify(result), result['status']

@user_blueprint.route('/login', methods=['POST'])
def login():
    data= request.get_json()
    result = authenticate_user(data)
    return jsonify(result), result["status"]