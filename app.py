from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello azure app'

@app.route('/azure')
def azure():
    return 'We are in azure!!!, making a change'
