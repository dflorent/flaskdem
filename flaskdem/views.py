from flaskdem import app

@app.route('/')
def index():
    return 'hi!'
