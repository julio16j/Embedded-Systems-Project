from flask import Flask, jsonify
import sys

from src.blueprints.user_blueprint import user_blueprint, USER_URL
from src.blueprints.swagger_blueprint import SWAGGER_URL, swagger_ui_blueprint
from src.api_spec import spec
from src.config.database_configuration import SQL_LITE_URL, setup_database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQL_LITE_URL
database = setup_database(app)

app.register_blueprint(user_blueprint, url_prefix=USER_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

with app.test_request_context():
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)

@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsonify(spec.to_dict())

with app.app_context():
    from src.model.entity.user import User
    database.create_all()
