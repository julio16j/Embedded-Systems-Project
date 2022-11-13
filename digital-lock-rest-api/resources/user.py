from flask_restful import Resource, reqparse

from models.user import UserModel


class Users(Resource):
    def get(self):
        return {'Users': [user.json() for user in UserModel.query.all()]}

class User(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('id_rfid_card')
    arguments.add_argument('name')

    def get(self):
        data = User.arguments.parse_args()
        user = UserModel.find_user(data['id_rfid_card'])
        if not (user is None):
            return user.json()
        return {'message': 'Not found'}, 404

    def post(self):
        data = User.arguments.parse_args()
        if UserModel.find_user(data['id_rfid_card']):
            return {'message': f'''User id '{data["id_rfid_card"]}' already exists.'''}, 400

        data = User.arguments.parse_args()
        user = UserModel(id_rfid_card=data['id_rfid_card'], name=data['name'])
        user.save_user()
        return user.json(), 201

    def put(self):
        data = User.arguments.parse_args()

        user = UserModel.find_user(data['id_rfid_card'])
        if user:
            user.update_user(data['id_rfid_card'],data['name'])
            user.save_user()
            return user.json(), 200
        user = UserModel(data['id_rfid_card'],data['name'])
        user.save_user()
        return user.json(), 200

    def delete(self):
        data = User.arguments.parse_args()
        user = UserModel.find_user(data['id_rfid_card'])
        if user:
            user.delete_user()
            return {'message': 'User deleted.'}, 200
        return {'message': 'User not found.'}, 404
        
