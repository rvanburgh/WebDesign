from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    migrate = Migrate(app, db)

    from flaskblog.users.routes import users
    from flaskblog.thoughts.routes import thoughts
    from flaskblog.burns_depression_test.routes import burns_depression_test
    from flaskblog.dysfunctional_attitude_scale.routes import dysfunctional_attitude_scale
    from flaskblog.gratitudes.routes import gratitudes
    from flaskblog.gdpr.routes import gdpr
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(thoughts)
    app.register_blueprint(burns_depression_test)
    app.register_blueprint(dysfunctional_attitude_scale)
    app.register_blueprint(gratitudes)
    app.register_blueprint(gdpr)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
