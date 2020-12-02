from flask import Flask, render_template, request
from flask.helpers import url_for
from flask.signals import request_tearing_down
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    todo_text = db.Column(db.String(100), index = True)


class TodoForm(FlaskForm):
    todo = StringField("Veteran")
    submit = SubmitField("Add Veteran")

db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

'''
@app.route('/home', methods=["GET", "POST"])
def index():
    if 'todo' in request.form:
        db.session.add(Todo(todo_text=request.form['todo']))
        db.session.commit()
    return render_template('home.html', todos=Todo.query.all(), template_form=TodoForm())
'''

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')