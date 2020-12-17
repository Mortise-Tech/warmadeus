#warmade_site/model.py
from . import init_app as app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
"""
db.session.add()
db.session.commit()
"""

class Product(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(50), index=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username