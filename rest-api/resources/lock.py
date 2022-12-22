from flask_restful import Resource, reqparse
from models.lock import LockModel


class Locks(Resource):
    def get(self):
        return {'Locks': [lock.json() for lock in LockModel.query.all()]}

class Lock(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('name')

    def get(self):
        data = Lock.arguments.parse_args()
        lock = LockModel.find_lock(data['name'])
        if not (lock is None):
            return lock.json()
        return {'message': 'Not found'}, 404

    def post(self):
        data = Lock.arguments.parse_args()
        if LockModel.find_lock(data['name']):
            return {'message': f'''Lock name '{data["name"]}' already exists.'''}, 400

        lock = LockModel(name=data['name'])
        lock.save_lock()
        return lock.json(), 201

    def put(self):
        data = Lock.arguments.parse_args()
        lock = LockModel.find_lock(data['name'])
        if lock:
            lock.update_lock(data['name'])
            lock.save_lock()
            return lock.json(), 200
            
        lock = LockModel(data['name'])
        lock.save_lock()
        return lock.json(), 201

    def delete(self):
        data = Lock.arguments.parse_args()
        lock = LockModel.find_lock(data['name'])
        if lock:
            lock.delete_lock()
            return {'message': 'Lock deleted.'}, 200
        return {'message': 'Lock not found.'}, 404
        
