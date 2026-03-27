from flask import Flask
app = Flask(__name__)

@app.route('/')
def name():
    return 'HI...THIS IS MY FIRST FLASK APP'