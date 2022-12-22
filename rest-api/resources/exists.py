from flask_restful import Resource, reqparse
from models.scheduled_time import ScheduledTimeModel
from datetime import datetime


class Exists(Resource):

    def get(self, id_rfid_card, lock_name):
        scheduled_time = ScheduledTimeModel.find_scheduled_time(id_rfid_card, lock_name)

        if not (scheduled_time is None):
            now_datetime = datetime.now()
            initial_datetime = scheduled_time.initial_datetime
            end_datetime = scheduled_time.end_datetime
            if (now_datetime >= initial_datetime and now_datetime <= end_datetime):
                return {'message': 'Allowed.'}, 200
        return {'message': 'Denied'}, 400