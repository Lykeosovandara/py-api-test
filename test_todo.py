import requests
from config import config


def test_todo():
    r = requests.get(f'{config.API_URL}/todos/1')
    assert r.status_code == 200, "Response is not 200"
    assert "userId" in r.json() , "userId is not response"
    assert "id" in r.json() , "id is not response"
    
def test_todo():
    r = requests.get(f'{config.API_URL}/todos')
    assert r.status_code == 200, "Response is not 200"
    assert isinstance(r.json(), list), "Response is not a list"
    