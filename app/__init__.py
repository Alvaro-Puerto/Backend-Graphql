import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView

from config import Development

from flask_graphql_auth import (
    AuthInfoField,
    GraphQLAuth,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    query_header_jwt_required,
    mutation_jwt_refresh_token_required,
    mutation_jwt_required
)

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Development)

    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        db.create_all()

    from app.graphql.schema import schema
    app.add_url_rule(
            "/graphql",
            view_func=GraphQLView.as_view(
                "graphql",
                schema=schema,
                graphiql=True
            )
        )
    
    return app
