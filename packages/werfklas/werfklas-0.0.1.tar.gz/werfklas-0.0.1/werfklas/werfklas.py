# Hier komt alles samen
from flask import Flask, render_template
from flask_assets import Environment  # Import `Environment`
from flask_bootstrap import Bootstrap

import frontend.children.routes
import frontend.families.routes
import frontend.teachers.routes
import frontend.classrooms.routes
from src.modules.common import find_waiting_children
from src.classes.database import create_database, sessionSetup


def create_app():
    """Create Flask application."""
    _app = Flask(__name__, instance_relative_config=False)
    _app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'
    assets = Environment()  # Create an assets environment
    assets.init_app(_app)  # Initialize Flask-Assets

    with _app.app_context():
        # Import parts of our application
        from frontend.teachers import routes
        from frontend.classrooms import routes
        from frontend.children import routes
        from frontend.families import routes

        # Register Blueprints
        _app.register_blueprint(frontend.teachers.routes.teachers_bp)
        _app.register_blueprint(frontend.classrooms.routes.classes_bp)
        _app.register_blueprint(frontend.children.routes.children_bp)
        _app.register_blueprint(frontend.families.routes.families_bp)

        return _app


app = create_app()
app.config['SECRET_KEY'] = 'MLXH243GssUWwKdTWS7FDhdwYF56wPj8'
Bootstrap(app)
databasefile = 'werfklas.db'
session = sessionSetup()


@app.route('/')
def index():
    _waiting_children = find_waiting_children()
    return render_template('index.html',
                           children=_waiting_children,
                           _PageTitle='Wachtlijst')


if __name__ == '__main__':
    from os.path import exists

    file_exists = exists(databasefile)
    if not file_exists:
        print(f'Database aanmaken..')
        create_database(databasefile=databasefile)
    app.run(debug=True)
