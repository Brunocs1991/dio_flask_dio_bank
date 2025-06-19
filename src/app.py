from flask import Flask,  url_for, request

app = Flask(__name__)


@app.route('/hello/<username>/<int:age>/<float:height>')
def hello_world(username, age, height):
    print(age)
    print(f'type of username: {type(username)}')
    print(f'type of age: {type(age)}')
    print(f'type of height: {type(height)}')
    return f'<p>Hello, World! user {username.upper()}</p>'


@app.route('/home')
def home():
    return '<p>Welcome to the Home Page!</p>'


@app.route('/projects/')
def projects():
    return '<p>Welcome to the Projects Page!</p>'


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        return '<p>About Page - POST method</p>'
    else:
        return '<p>Welcome to the About Page!</p>'


with app.test_request_context():
    print(url_for('hello_world', username='John', age=30, height=5.9))
    print(url_for('home'))
    print(url_for('projects'))
    print(url_for('about', next='/'))
