from sql_alchemy import bd
from models.lock import LockModel
from models.user import UserModel
from datetime import datetime
class ScheduledTimeModel(bd.Model):
    __tablename__ = 'scheduled_time'

    id_scheduled_times = bd.Column(bd.Integer,primary_key=True)
    id_user = bd.Column(bd.Integer)
    id_lock = bd.Column(bd.Integer)
    initial_datetime = bd.Column(bd.DateTime)
    end_datetime = bd.Column(bd.DateTime)
    

    def __init__(self,id_user, id_lock, initial_datetime, end_datetime) -> None:
        self.id_user = id_user
        self.id_lock = id_lock
        self.initial_datetime = initial_datetime
        self.end_datetime = end_datetime
        
    def json(self):
        return {
            'id_user': self.id_user,
            'id_lock': self.id_lock,
            'initial_datetime': str(self.initial_datetime),
            'end_datetime': str(self.end_datetime)
        }

    @classmethod
    def find_scheduled_time(cls, id_rfid_card, lock_name):
        lock_founded = LockModel.find_lock(name=lock_name)
        user_founded = UserModel.find_user(id_rfid_card=id_rfid_card)
        if not (lock_founded and user_founded):
            return None
        scheduled_time = cls.query.filter_by(id_user=user_founded.id_user,
            id_lock=lock_founded.id_lock).first()
        if scheduled_time:
            return scheduled_time
        return None

    def save_scheduled_time(self):
        bd.session.add(self)
        bd.session.commit()

    def update_scheduled_time(self,initial_datetime, end_datetime):
        self.initial_datetime = initial_datetime
        self.end_datetime = end_datetime

    def delete_scheduled_time(self):
        bd.session.delete(self)
        bd.session.commit()