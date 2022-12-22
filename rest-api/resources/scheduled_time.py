from datetime import datetime
from flask_restful import Resource, reqparse
from models.user import UserModel
from models.lock import LockModel
from models.scheduled_time import ScheduledTimeModel

class ScheduledTimes(Resource):
    def get(self):
        return {'ScheduledTimes': [scheduled_time.json() for scheduled_time in ScheduledTimeModel.query.all()]}

# arrumar os metodos para receber o id do usuario e o id da fechadura 
# um endpoint pra o microcontrolador consultar: vai passar o id do usuário e o nome da fechadura
class ScheduledTime(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('id_rfid_card')
    arguments.add_argument('lock_name')
    arguments.add_argument('initial_datetime', type=lambda date: datetime.strptime(date, '%d/%m/%Y %H:%M'))
    arguments.add_argument('end_datetime', type=lambda date: datetime.strptime(date, '%d/%m/%Y %H:%M'))

    def get(self):
        data = ScheduledTime.arguments.parse_args()
        scheduled_time = ScheduledTimeModel.find_scheduled_time(data['id_rfid_card'], data['lock_name'])
        if not (scheduled_time is None):
            return scheduled_time.json()
        return {'message': 'Not found'}, 404

    def post(self):
        data = ScheduledTime.arguments.parse_args()
        id_rfid_card = data['id_rfid_card']
        lock_name = data['lock_name']
        initial_datetime = data['initial_datetime']
        end_datetime = data['end_datetime']
        lock_founded = LockModel.find_lock(name=lock_name)
        user_founded = UserModel.find_user(id_rfid_card=id_rfid_card)
        scheduled_times = ScheduledTimeModel.find_scheduled_times(id_rfid_card,lock_name)
        for scheduled_time in scheduled_times:
            if scheduled_time.initial_datetime == initial_datetime and (
                scheduled_time.end_datetime == end_datetime):
                return {'message': f'This scheduled time already exists.'}, 400

        scheduled_time = ScheduledTimeModel(id_lock=lock_founded.id_lock, id_user=user_founded.id_user,
            initial_datetime=initial_datetime, end_datetime=end_datetime)
        scheduled_time.save_scheduled_time()
        return scheduled_time.json(), 201

    def put(self):
        data = ScheduledTime.arguments.parse_args()
        id_rfid_card = data['id_rfid_card']
        lock_name = data['lock_name']
        initial_datetime = data['initial_datetime']
        end_datetime = data['end_datetime']
        scheduled_time = ScheduledTimeModel.find_scheduled_time(id_rfid_card, lock_name)
        if scheduled_time:
            scheduled_time.update_scheduled_time(initial_datetime, end_datetime)
            scheduled_time.save_scheduled_time()
            return scheduled_time.json(), 200

        
        lock_founded = LockModel.find_lock(name=lock_name)
        user_founded = UserModel.find_user(id_rfid_card=id_rfid_card)
        scheduled_time = ScheduledTimeModel(id_lock=lock_founded.id_lock, id_user=user_founded.id_user,
            initial_datetime=initial_datetime, end_datetime=end_datetime)
        scheduled_time.save_scheduled_time()
        return scheduled_time.json(), 201

    def delete(self):
        data = ScheduledTime.arguments.parse_args()
        scheduled_time = ScheduledTimeModel.find_scheduled_time(data['id_rfid_card'], data['lock_name'])
        if scheduled_time:
            scheduled_time.delete_scheduled_time()
            return {'message': 'ScheduledTime deleted.'}, 200
        return {'message': 'ScheduledTime not found.'}, 404
        
