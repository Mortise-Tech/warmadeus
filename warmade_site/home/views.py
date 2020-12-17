# home/views.py
from flask import Blueprint, render_template

home_bp = Blueprint(
    'home_bp',
    __name__,
    static_folder='static',
    template_folder='templates'
    )

@home_bp.route('/', methods=["GET"])
def index():
    """HOMEPAGE."""
    return render_template('index.html')