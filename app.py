from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the database
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id} - {self.title}"

# Input validation function
def validate_input(input_string):
    # You can customize this function to fit your specific validation needs
    return input_string.strip()

@app.route('/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        title = validate_input(request.form['title'])
        desc = validate_input(request.form['desc'])
        todo = TodoModel(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    alltodo = TodoModel.query.all()
    return render_template('index.html', alltodo=alltodo)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        title = validate_input(request.form['title'])
        desc = validate_input(request.form['desc'])
        todo = TodoModel.query.get(id)
        if todo:
            todo.title = title
            todo.desc = desc
            db.session.commit()
        return redirect(url_for('Home'))
    
    todo = TodoModel.query.get(id)
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    todo = TodoModel.query.get(id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('Home'))

@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('search')
    if search_query:
        search_query = f"%{validate_input(search_query)}%"  # Adding wildcard '%' for partial matching
        todos = TodoModel.query.filter(TodoModel.title.like(search_query)).all()
        return render_template('search.html', todos=todos)
    return redirect(url_for('Home'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
