from flask import Flask
from flask_pg_extras import FlaskPGExtras

flask_pg_extras = FlaskPGExtras()


def create_app():
    app = Flask(__name__)

    flask_pg_extras.init_app(app)

    @app.route('/')
    def index():
        return 'Hello world'

    return app
