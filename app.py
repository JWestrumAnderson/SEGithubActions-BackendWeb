"""_summary_ Returns: _type_: _description_"""
from datetime import date
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def load_page():
    """Creates 3 links to pages"""
    return '<a href="/page1">P1</a><a href="/p2">Page2</a><a href="/p3">Page3</a><h1>Main</h1>'


@app.route("/p1")
def page_one():
    """Creates todays date and displays"""
    today = date.today()
    return f'<a href="/">Load Page</a><h1>Todays Date: {today}</h1>'


@app.route("/p2")
def page_two():
    """Takes todays date and isolates/displays month"""
    month = date.today()
    month = month.strftime("%B")
    return f'<a href="/">Load Page</a><h1>Month is: {month}</h1>'


@app.route("/p3")
def page_three():
    """Takes todays date and isolates/displays weekday"""
    day = date.today()
    day = day.strftime("%A")
    return f'<a href="/">Load Page</a><h1>Weekday is: {day}</h1>'
