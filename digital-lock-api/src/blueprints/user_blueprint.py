from flask import Blueprint, jsonify, request
from flask_restful import reqparse

user_blueprint = Blueprint(name="user_blueprint", import_name=__name__)
user = {'name': 'joao_henrique'}
USER_URL = "/api/user"

@user_blueprint.route('/', methods=['GET'])
def get_user():
    """
    ---
    get:
      description: get user
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User
    """
    output = user
    return jsonify(output)

@user_blueprint.route('/', methods=['POST'])
def save_user():
    """
    ---
    post:
      description: save user
      requestBody:
        required: true
        content:
            application/json:
                schema: UserSchema
      responses:
        '200':
          description: call successful
          content:
            application/json:
              schema: UserSchema
      tags:
          - User
    """
    arguments = reqparse.RequestParser()
    arguments.add_argument('key')
    arguments.add_argument('username')

    data = arguments.parse_args()

    new_user = {
      'key': data['key'],
      'username': data['username']
    }
    data = request.get_json()
    user['name'] = data['name']
    output = {"msg": f"New user saved: '{user}'"}
    return jsonify(output)