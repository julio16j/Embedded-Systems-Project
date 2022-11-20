from flask_restful import Resource, reqparse
from models.scheduled_time import ScheduledTimeModel
from datetime import datetime


class Exists(Resource):
    arguments = reqparse.RequestParser()
    arguments.add_argument('id_rfid_card')
    arguments.add_argument('lock_name')

    def get(self):
        data = Exists.arguments.parse_args()
        scheduled_time = ScheduledTimeModel.find_scheduled_time(data['id_rfid_card'], data['lock_name'])

        if not (scheduled_time is None):
            now_datetime = datetime.now().strftime('%d/%m/%Y %H:%M').split(' ')
            initial_datetime = scheduled_time.initial_datetime.strftime('%d/%m/%Y %H:%M').split(' ')
            end_datetime = scheduled_time.end_datetime.strftime('%d/%m/%Y %H:%M').split(' ')

            if initial_datetime[0] == now_datetime[0]:
                now_time = now_datetime[1].split(':')
                initial_time = initial_datetime[1].split(':')
                end_time = end_datetime[1].split(':')

                if now_time[0] >= initial_time[0] and now_time[0] <= end_time[0]:
                    if now_time[1] >= initial_time[1]:
                        return {'message': 'Allowed.'}, 200
                
        return {'message': 'Denied'}, 400