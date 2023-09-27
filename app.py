from flask import Flask, request
from datetime import date

app = Flask(__name__)


@app.route("/")
def loadPage():
    """Creates 3 links to pages"""
    return '<a href="/pageOne">Page 1</a><a href="/pageTwo">Page 2</a><a href="/pageThree">Page 3</a><h1>Load Page</h1>'


@app.route("/pageOne")
def pageOne():
    """Creates todays date and displays"""
    today = date.today()
    return f'<a href="/">Load Page</a><h1>Todays Date: {today}</h1>'


@app.route("/pageTwo")
def pageTwo():
    """Takes todays date and isolates/displays month"""
    month = date.today()
    month = month.strftime("%B")
    return f'<a href="/">Load Page</a><h1>Month is: {month}</h1>'


@app.route("/pageThree")
def pageThree():
    """Takes todays date and isolates/displays weekday"""
    day = date.today()
    day = day.strftime("%A")
    return f'<a href="/">Load Page</a><h1>Weekday is: {day}</h1>'
