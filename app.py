# flask Minimal app code 
from flask import Flask, render_template

# app is an instance of the Flask class which is a WSGI application
# WSGI is a specification for a universal interface between the web server and the web application
app = Flask(__name__)
@app.route('/')

def Home():
    return render_template('index.html')

# @route is a decorator which tells the app which URL should call the associated function 
@app.route('/products')
def Products():
    return ('Products')


# this is the main app which will run the app
# __name__ is a special variable in python which is the name of the module
# which is being run. If it is being run from the command line, then __name__ = __main__
if __name__ == '__main__':
    app.run(debug=True)

    


