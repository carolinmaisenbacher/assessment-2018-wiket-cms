from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config = Config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints here
    from app.authentification import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from app.main import blueprint as main_blueprint
    app.register_blueprint(main_blueprint)

    # everything in here will be skipped when testing
    if not app.debug and not app.testing:
        pass

    return app