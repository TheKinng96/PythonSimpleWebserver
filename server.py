from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<username>/<int:post_id>')
def blog(username=None, post_id=None):
    return render_template('name.html', name=username, post_id=post_id)
