# Introduction to Flask and Flask-RESTful

# steps to Install and run Hello World Flask App
- Install Flask By running the command `pip install Flask`
- Create a file called `app.py`
- Import Flask and create an instance of Flask
- Create a function that returns a string

# Important Notes
- Flask is a microframework
- Flask is a class  
- Flask is used to create web servers 
- Flask is used to create an instance of web application
- Flask is used to create web applications
- Flask is used to create APIs
- Flask is used to create web services
- Flask is used to create web resources
- Flask is used to create web pages


# Creating A database using Flask SQLAlchemy

- for creating a database using Flask SQLAlchemy we need to install SQLAlchemy by running the command `pip install SQLAlchemy`
- SQLAlchemy is a Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.
- SQLAlchemy provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
- SQLAlchemy provides a generalized interface for creating and executing database-agnostic code without needing to write SQL statements.
- SQLAlchemy provides a core level of service, independent of the database engine used, which can be extended through the use of optional components such as ORM and database schema definition.

# On Linux 
- If you are unable to create a database using python shell it shows error sometimes 
- Use flask Shell and create a database  (db.create_all())
- 

# Flask-RESTful

- Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
- Flask-RESTful encourages best practices with minimal setup. If you are familiar with Flask, Flask-RESTful should be easy to pick up. It provides a coherent collection of decorators and tools to describe your API and expose its documentation properly (using Swagger).
- Flask-RESTful provides the flexibility of using different HTTP request methods such as GET, POST, DELETE, PUT, PATCH, OPTIONS, etc. to perform different actions.
- Flask-RESTful also provides support for custom request data such as JSON, XML, YAML, etc. because of its built-in request parsing.
- Flask-RESTful also provides support for custom response data such as JSON, XML, YAML, etc. because of its built-in response formatting.
- Flask-RESTful also provides support for custom error handling.
- Flask-RESTful also provides support for custom authentication and authorization.
- Flask-RESTful also provides support for custom URL routing.

# install Jinja2 for Flask Templates
- Jinja2 is a template engine for Python. It is a text-based template language and thus can be used to generate any markup as well as source code.
- Jinja2 is one of the most used template engines for Python. It is inspired by Django’s templating system but extends it with an expressive language that gives template authors a more powerful set of tools.
- Jinja2 is a full-featured template engine for Python. It has full unicode support, an optional integrated sandboxed execution environment, widely used and BSD licensed.
- Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django’s templates. It is fast, widely used and secure with the optional sandboxed template execution environment.
- Jinja2 is a template engine written in pure Python. It provides a Django inspired non-XML syntax but supports inline expressions and an optional sandboxed environment.

# Filters in Jinja2

- Jinja2 ships with many of filters. Filters in Jinja2 are a way of transforming template expressions from one kind of data into another. They are similar to functions in that they take arguments and produce an output. Filters are separated from the variable by a pipe symbol (|) and may have optional arguments in parentheses. Multiple filters can be chained. The output of one filter is applied to the next.

# Template Inheritence in jinja2
- Jinja2 supports template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override.
- Jinja2 is a template engine for Python. It is a text-based template language and thus can be used to generate any markup as well as source code.
- Jinja2 is one of the most used template engines for Python. It is inspired by Django’s templating system but extends it with an expressive language that gives template authors a more powerful set of tools.

# Gunicorn an Amazing WSGI HTTP Server for Python
- it can be installed by running the command `pip install gunicorn`
- it will show the requirement of your project in a seprate file 
- it will also show the version of gunicorn you are using
- 
## A table which contain For prerequisite and installation of Flask and Flask-RESTful

| Prerequisite | Installation |
| --- | --- |
| Python | [Python](https://www.python.org/downloads/) |
| Flask | `pip install Flask` |
| Flask-RESTful | `pip install Flask-RESTful` |


# Deployement of Flask App on Heroku
- Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.
- Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.
- Steps to deploy a Flask App on Heroku
- 1. Create a Heroku Account
- 2. Install Heroku CLI
- 3. Create a Heroku App
- 4. Create a requirements.txt file
- 5. Create a Procfile
- 6. Push the code to Heroku
- 7. Visit the URL of the application
- 8. View the logs
- 9. Scale the application
- 10. Define Config Variables
- 11. Deploying a Flask App on Heroku
