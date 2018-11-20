from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#added by julian in order to have access to backend
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config = Config):
    app = Flask(__name__)
    
    #added by julian in order to have access to backend
    cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints here
    from app.authentification import blueprint as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from app.main import blueprint as main_blueprint
    app.register_blueprint(main_blueprint)
    from app.api import blueprint as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # everything in here will be skipped when testing
    if not app.debug and not app.testing:
        pass

    return app
