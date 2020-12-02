from flask import Flask
from home.home import home_bp

app = Flask(__name__)

app.register_blueprint(home_bp)