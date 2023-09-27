import pytest
from app import app
from datetime import date


def test_today(client):
    response = client.get("/pageOne")
    today = date.today()
    assert today in response.data


def test_Month(client):
    response = client.get("/pageTwo")
    month = date.today()
    month = month.strftime("%B")
    assert month in response.data


def test_Month(client):
    response = client.get("/pageTwo")
    weekday = date.today()
    weekday = weekday.strftime("%A")
    assert weekday in response.data
