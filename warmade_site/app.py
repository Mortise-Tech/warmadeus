from flask import Flask

from home.views import home_bp
from auth.views import auth_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)