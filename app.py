from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def loadPage():
    return '<a href="/pageOne">Page 1</a><a href="/pageTwo">Page 2</a><a href="/pageThree">Page 3</a><h1>Page One</h1><input type="text" id="num1" placeholder="Enter first Number"/><input type="text" id="num2" placeholder="Enter second Number"/>'


@app.route("/pageOne")
def pageOne():
    today = date.today()
    return '<a href="/">Load Page</a><h1>Todays Date: {today}</h1>'


@app.route("/pageTwo")
def pageTwo():
    num1 = 0
    num2 = 1
    addNum = num1 + num2
    return '<a href="/">Load Page</a><h1>Number is: {addNum}</h1>'


@app.route("/pageThree")
def pageThree():
    day = date.today()
    day = day.strftime("%A")
    return '<a href="/">Load Page</a><h1>Weekday is: {day}</h1>'
