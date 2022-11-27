from sql_alchemy import bd

class LockModel(bd.Model):
    __tablename__ = 'locks'

    id_lock = bd.Column(bd.Integer,primary_key=True)
    name = bd.Column(bd.String(80))
    
    def __init__(self,name) -> None:
        self.name = name
        
    def json(self):
        return {
            'name': self.name
        }

    @classmethod
    def find_lock(cls, name):
        lock = cls.query.filter_by(name=name).first()
        if lock:
            return lock
        return None

    def save_lock(self):
        bd.session.add(self)
        bd.session.commit()

    def update_lock(self,name):
        self.name = name

    def delete_lock(self):
        bd.session.delete(self)
        bd.session.commit()