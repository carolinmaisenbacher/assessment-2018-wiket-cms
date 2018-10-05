from flask import Flask
from .settings import DATABASE_HOST, DATABASE_NAME, DATABASE_SECRET, DATABASE_USER
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USER}:{DATABASE_SECRET}@{DATABASE_HOST}/{DATABASE_NAME}"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # register blueprints here
# from app.authentification import blueprint as auth_blueprint
# app.register_blueprint(auth_blueprint, url_prefix='/auth')
# from app.main import blueprint as main_blueprint
# app.register_blueprint(main_blueprint)


# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DATABASE_USER}:{DATABASE_SECRET}@{DATABASE_HOST}/{DATABASE_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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