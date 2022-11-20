from sql_alchemy import bd

class UserModel(bd.Model):
    __tablename__ = 'users'

    id_user = bd.Column(bd.Integer,primary_key=True)
    id_rfid_card = bd.Column(bd.String(80))
    name = bd.Column(bd.String(80))
    
    def __init__(self,id_rfid_card,name) -> None:
        self.id_rfid_card = id_rfid_card
        self.name = name
        
    def json(self):
        return {
            'id_rfid_card': self.id_rfid_card,
            'name': self.name
        }

    @classmethod
    def find_user(cls, id_rfid_card):
        user = cls.query.filter_by(id_rfid_card=id_rfid_card).first()
        if user:
            return user
        return None

    def save_user(self):
        bd.session.add(self)
        bd.session.commit()

    def update_user(self,id_rfid_card,name):
        self.id_rfid_card = id_rfid_card
        self.name = name

    def delete_user(self):
        bd.session.delete(self)
        bd.session.commit()