from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields

spec = APISpec(
    title="Tranca Digital Api",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

class UserSchema(Schema):
    name = fields.String(description="username")

spec.components.schema("User", schema=UserSchema())
tags = [
            {'name': 'User',
             'description': 'primeiramente para testes'
            }
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)