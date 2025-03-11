import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'токен'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = "22893"
STATUSPOKEMONS = "1"  #status=0 - покемон в нокауте;

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers= HEADER, params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200
    assert response.json()["data"][0]["trainer_name"] == "Чухня Всемогущий"

@pytest.mark.parametrize('key, value', [('trainer_name', "Чухня Всемогущий")])
def test_parametrize(key, value):
    responsep = requests.get(url = f'{URL}/trainers', params={"trainer_id": TRAINER_ID})
    assert responsep.json()["data"][0][key] == value 