from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/pageOne")
def pageOne():
    return "<p>Page One</p>"

@app.route("/pageTwo")
def pageTwo():
    return "<p>Page Two</p>"

@app.route("/pageThree")
def pageThree():
    return "<p>Page Three</p>"
