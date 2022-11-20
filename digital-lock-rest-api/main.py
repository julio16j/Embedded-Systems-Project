from flask import Flask
from flask_restful import Api

from resources.user import Users, User
from resources.lock import Locks, Lock
from resources.sheduled_time import ScheduledTimes, ScheduledTime
from resources.exists import Exists


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_db():
    bd.create_all()


api.add_resource(Users,'/api/users')
api.add_resource(User,'/api/user')
api.add_resource(Locks,'/api/locks')
api.add_resource(Lock,'/api/lock')
api.add_resource(ScheduledTimes,'/api/scheduled-times')
api.add_resource(ScheduledTime,'/api/scheduled-time')
api.add_resource(Exists,'/api/exists')


if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(debug=True)