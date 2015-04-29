from flaskdem import app
from flask import render_template, url_for

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello/index.html', name=name)