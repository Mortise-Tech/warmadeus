# about/views.py
from flask import Blueprint, render_template

about_bp = Blueprint(
    'about',
    __name__,
    static_folder='static',
    template_folder='templates/about',
    url_prefix='/about'
    )

@about_bp.route('/')
def index():
    return render_template('index.html')