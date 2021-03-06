from flask import Blueprint, request, jsonify
from models.User import User, UserSchema
from datetime import datetime, timedelta
import jwt
from config.environment import secret
from marshmallow import ValidationError

user_schema = UserSchema()

api = Blueprint('auth', __name__)


def create_token(user):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user.id
    }

    token = jwt.encode(
        payload,
        secret,
        'HS256'
    ).decode('utf-8')

    return token


@api.route('/register', methods=['POST'])
def register():
    try:
        data = user_schema.load(request.get_json())
    except ValidationError as error:
        return jsonify({'error': error.messages}), 422

    user = User(data)
    user.save()

    return jsonify({
        'message': 'Registation successful',
        'token': create_token(user)
    })


@api.route('/login', methods=['POST'])
def login():

    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    if not user or not user.validate_password(data.get('password', '')):
        return jsonify({'message': 'Unauthorized'}), 401

    return jsonify({
        'message': 'Welcome back {}!'.format(user.username),
        'token': create_token(user)
    })
