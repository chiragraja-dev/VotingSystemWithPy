from app.utils.db import get_db
from app.models.user_model import User
from flask_bcrypt import Bcrypt
from app.utils.helper import generate_token
import re

bcrypt=Bcrypt()

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def create_user(data):
    db= get_db()
    user = db.user.find_one({"email":data['email']})
    if user:
        return {"status":400,"message":"User already exists."}

    if data['role'] not in ["admin", "voter"]:
        return {"status":400,"message":"invalid role"}
    
    if not validate_email(data['email']):
        return {"status":400, "message":"invalid email"}

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(
        fullName=data['fullName'],
        email=data['email'],
        password=hashed_password,
        role=data['role']
    )
    db.user.insert_one(new_user.__dict__)
    token = generate_token(new_user.email, new_user.role)
    return {"status":201, "message":"user created", "token":token}

def authenticate_user(data):
    db= get_db()
    user = db.user.find_one({'email':data['email']})
    if not user or not bcrypt.check_password_hash(user['password'],data['password']):
        return {"status":401, "message":"Invalid email or password"}
    token = generate_token(data['email'], data['role'])
    return {"status":201, "message":"login successfully", "token":token}


    
