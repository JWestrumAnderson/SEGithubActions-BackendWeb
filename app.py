from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)


@app.route("/")
def loadPage():
    return '<a href="/pageOne">Page 1</a><a href="/pageTwo">Page 2</a><a href="/pageThree">Page 3</a><h1>Load Page</h1>'


@app.route("/pageOne")
def pageOne():
    today = date.today()
    return f'<a href="/">Load Page</a><h1>Todays Date: {today}</h1>'


@app.route("/pageTwo")
def pageTwo():
    month = date.today()
    month = month.strftime("%B")
    return f'<a href="/">Load Page</a><h1>Month is: {month}</h1>'


@app.route("/pageThree")
def pageThree():
    day = date.today()
    day = day.strftime("%A")
    return f'<a href="/">Load Page</a><h1>Weekday is: {day}</h1>'
