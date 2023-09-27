"""_summary_ Returns: _type_: _description_"""
from datetime import date
import pytest
from app import app


@pytest.fixture()
def client():
    return app.test_client()    

def test_today(client):
    """Verifies todays date"""
    response = client.get("/pageOne")
    today = date.today()
    assert today in response.data


def test_month(client):
    """Verifies the month"""
    response = client.get("/pageTwo")
    month = date.today()
    month = month.strftime("%B")
    assert month in response.data


def test_weekday(client):
    """Verifies the weekday"""
    response = client.get("/pageTwo")
    weekday = date.today()
    weekday = weekday.strftime("%A")
    assert weekday in response.data
