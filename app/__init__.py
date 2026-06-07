from flask import Flask
from config import Config
from app.models import db
from app.auth import auth
from app.main import main
from app.booking import booking
from app.admin import admin
from app.extensions import db,bcrypt,login_manager,mail



def create_app():
    #create app
    app = Flask(__name__)
    
    #load configs
    app.config.from_object(Config)

    #init extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    mail.init_app(app)

    #register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(booking)
    app.register_blueprint(admin)

    with app.app_context():
        db.create_all()

    return app
