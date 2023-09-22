import os

from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemy
db = SQLAlchemy()

# Migrate
migrate = Migrate()

# Mail
mail = Mail()


def create_app():
    app = Flask(__name__, static_folder="static", template_folder="views")

    # SECRET_KEY
    app.config["SECRET_KEY"] = "2FGEYqGuC@y1hL*%jNSdf%#t"

    # DATABASE
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://postgres:postgres@localhost/imoveis-dev"

    # DATABASE SQLITE
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # CSRFProtect
    # csrf (cross-site request forgery)
    # csrf.init_app(app)

    # Email
    app.config["MAIL_SERVER"] = "smtp.mailtrap.io"
    app.config["MAIL_PORT"] = 587
    app.config["MAIL_USERNAME"] = "d1dfeade58bfa5"
    app.config["MAIL_PASSWORD"] = "3409468f9aef90"
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False

    # Mail
    mail.init_app(app)

    # SQLAlchemy
    db.init_app(app)

    # Migrate
    migrate.init_app(app, db)

    # Rotas
    from app.controllers import routes

    routes.init_app(app)

    return app
