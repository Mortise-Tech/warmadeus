# warmade_site/__init__
import os
from flask import Flask
from flask_assets import Environment

def init_app():
    # Create Flask app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.default') # use default config
    app.config.from_pyfile('config.py') # settings from instance
    #assets = Environment()
    #assets.init_app(app)

    # Import Blueprints
    from .home.views import home_bp

    # Register Blueprints
    app.register_blueprint(home_bp)

    # Compile static assests
    #compile_static_assets(assets)

    return app