# flask Minimal app code 
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# this is the model for the database    
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.id} - {self.title}"


@app.route('/')
def Home():
    todo = TodoModel(title="first name ", desc= "Start Investing in stock exchange")
    db.session.add(todo)
    db.session.commit()

    return render_template('index.html')

# @route is a decorator which tells the app which URL should call the associated function 
@app.route('/show')
def Products():
    alltodo= TodoModel.query.all()
    print(alltodo)
    return ('Products')


# this is the main app which will run the app
if __name__ == '__main__':
    app.run(debug=True)

    


