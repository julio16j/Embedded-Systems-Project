from src.app import database

class User(database.Model):
    key = database.Column(database.String, primary_key=True)
    username = database.Column(database.String,nullable=False)
    