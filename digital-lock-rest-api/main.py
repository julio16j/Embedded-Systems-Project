from flask import Flask
from flask_restful import Api

from resources.user import Users, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_first_request
def create_db():
    bd.create_all()


api.add_resource(Users,'/api/users')
api.add_resource(User,'/api/user')


if __name__ == '__main__':
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(debug=True)