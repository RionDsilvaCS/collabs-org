from flask import Blueprint
from config import db
# from config import jwt
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask import jsonify
from flask import request

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/')
def test():
    return "auth route"

@auth_blueprint.route("/member-login", methods=["POST"])
def member_login():
    cursor = db.connection.cursor()
    id_ = 0
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    query = "SELECT * FROM member WHERE email = %s and pass_word = %s"
    arg = (username, password)
    cursor.execute(query, arg)
    if cursor.rowcount == 0:
        return jsonify({"msg": "Bad username or password"})
    for c in cursor:
        id_ = c[0]
        print(id_)
    id_ = f'{id}_m'
    access_token = create_access_token(identity=id_)
    return jsonify(access_token=access_token, role="member"), 200

@auth_blueprint.route("/lead-login", methods=["POST"])
def lead_login():
    cursor = db.connection.cursor()
    id_ = 0
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    query = "SELECT * FROM Team_Lead WHERE email = %s and pass_word = %s"
    arg = (username, password)
    cursor.execute(query, arg)
    if cursor.rowcount == 0:
        return jsonify({"msg": "Bad username or password"})
    for c in cursor:
        id_ = c[0]
        print(id_)
    
    id_ = f'{id}_l'
    access_token = create_access_token(identity=id_)
    return jsonify(access_token=access_token, role="lead"), 200

@auth_blueprint.route("/admin-login", methods=["POST"])
def admin_login():
    cursor = db.connection.cursor()
    id_ = 0
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    query = "SELECT * FROM Super_Admin WHERE email = %s and pass_word = %s"
    arg = (username, password)
    cursor.execute(query, arg)
    if cursor.rowcount == 0:
        return jsonify({"msg": "Bad username or password"})
    for c in cursor:
        id_ = c[0]
        print(id_)
    
    id_ = f'{id}_a'
    access_token = create_access_token(identity=id_)
    return jsonify(access_token=access_token, role="admin"), 200

@auth_blueprint.route("/protected", methods=["GET"])
@jwt_required()
def protected_test():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200