from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('../settings.py') # print app.config['FOO']

import flaskdem.views
import flaskdem.hello.views
