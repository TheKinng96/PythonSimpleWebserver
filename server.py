from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Yap!'


@app.route('/blog')
def blog():
    return 'This is the first blog.'
