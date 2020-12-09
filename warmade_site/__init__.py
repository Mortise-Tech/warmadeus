from flask import Flask
from flask.helpers import url_for

from .home.views import home_bp
#from .auth.views import auth_bp
from .about.views import about_bp


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.development') # use default config
app.config.from_pyfile('config.py') # settings from instance

# Load the file specified by the APP_CONFIG_FILE environment variable
#app.config.from_envvar('APP_CONFIG_FILE')


app.register_blueprint(home_bp)
#app.register_blueprint(auth_bp)
app.register_blueprint(about_bp)
