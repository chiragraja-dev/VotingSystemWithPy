import jwt
import datetime
from flask import current_app
from flask_bcrypt import Bcrypt

bcrypt=Bcrypt()

def generate_token(email,role):
    payload = {
        'email':email,
        'role':role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token

def compare_password(plain_pass, hashed_pass):
    return bcrypt.check_password_hash(hashed_pass,plain_pass)

def authenticate_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return {"email":payload['email'], 'role':payload['role']}
    except jwt.ExpiredSignature:
        return None
    except jwt.InvalidTokenError:
        return None