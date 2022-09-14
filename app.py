from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#first step in starting a flask app
app = Flask(__name__)

#configuring the database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///honey_todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#initializing sqlalchemy
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/')
def hello_world():
    todo = Todo(title="first Todo", desc="Start Investing in Stock Market")    
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all() 
    return render_template('index.html', allTodo=allTodo)

    
@app.route('/show')
def products():
    allTodo = Todo.query.all()  
    print(allTodo)
    return 'this is products page'

if __name__ == "__main__":
    app.run(debug=True)