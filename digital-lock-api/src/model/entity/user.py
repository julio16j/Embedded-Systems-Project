from src.app import database

class User(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, unique=True, nullable=False)
    key = database.Column(database.String)