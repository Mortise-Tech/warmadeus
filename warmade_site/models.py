from warmade_site.app import db, Todo

first_todo = Todo(todo_text="Create Website")

db.session.add(first_todo)
db.session.commit()

all_todo = Todo.query.all()
print(all_todo[0].todo_text)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(50), index=True)