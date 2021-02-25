from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import routes


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask("TestApp")
    app.config.from_object("config")

    if testing is True:
        app.config["TESTING"] = True


    # Database
    db = SQLAlchemy()
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    register_blueprints(app)

    dir(routes)
    return app

def register_blueprints(app):
    """register all blueprints for application"""
    #app.register_blueprint(views.blueprint)

