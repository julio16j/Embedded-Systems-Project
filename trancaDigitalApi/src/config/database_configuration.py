from flask_sqlalchemy import SQLAlchemy
SQL_LITE_URL = "sqlite:///project.db"

def setup_database (app_instance):
    database = SQLAlchemy()
    database.init_app(app_instance)
    return database
