import requests
import random


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'токен'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = "22893"
STATUSPOKEMONS = "1"  #status=0 - покемон в нокауте;


BODY_CREATE = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = BODY_CREATE)
print(response.text)

change_name = f"Bibizyanka{random.randint(1, 1000)}"

if response.json()["message"] == "Максимум 5 живых покемонов":
    print("Получаем список покемонов █▒▒▒▒▒▒▒▒▒ 11%")
    response_get_pokemons = requests.get(url= f'{URL}/pokemons', headers= HEADER, params={'trainer_id': TRAINER_ID, 'status': STATUSPOKEMONS})
    print(f'Response status get: {response_get_pokemons.status_code}, Response text get: {response_get_pokemons.text}')
    print("Отправляем покемона в нокаут █████████▒ 90%")

    GET_ID = response_get_pokemons.json()["data"][0]["id"]   
    print(GET_ID)
    
    BODY_DELETE = { 
    "pokemon_id": GET_ID
    }

    response_delete = requests.post(url = f"{URL}/pokemons/knockout", headers=HEADER, json=BODY_DELETE)
    print(f"Status code delete: {response_delete.status_code}, Response text delete: {response_delete.text}")
    print("██████████ 100% Покемон успешно удален")
else:
    response.json()["message"] == "Покемон создан"
    print("Превращаем покемона в брадка-обезьяну и присваиваем номер. ███████▒▒▒ 74%")
    
    POKEMON_ID = response.json()["id"]
    print(POKEMON_ID)

    change_pokemon_body = {
    "pokemon_id": POKEMON_ID,
    "name": change_name,
    "photo_id": -1
    }

    body_add_pokeball = {
        "pokemon_id": POKEMON_ID
    }


    response_change_pokemon = requests.put(url= f'{URL}/pokemons', headers= HEADER, json= change_pokemon_body)
    print(f'Response text change: {response_change_pokemon.text}, Status code change:{response_change_pokemon.status_code}, Response time change pokemon: {response_change_pokemon.elapsed.total_seconds()} seconds') 
    print("█████████▒ 93% Ловите его!!!!!")
    response_add_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_add_pokeball )
    print(f'Status Code add: {response_add_pokeball.status_code},  Response text add: {response_add_pokeball.text}, Response time add pokeball: {response_add_pokeball.elapsed.total_seconds()} seconds')
    print("██████████ 100% Перевоплощение в бибизянку успешно!")
    









