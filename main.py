import requests  

url = 'https://api.pokemonbattle.ru/v2' 
token = '2e46a45a4ed976e184a6d5a8eee8693f' 
header = {'Content-Type' : 'application/json', 'trainer_token' : token}

body_create = {
    "name": "Придумать имя",
    "photo_id": 6
}

body_rename = {
    "pokemon_id": "ID Покемона из списка",
    "name": "Чаризард",
    "photo_id": 6
}

body_catch = {
    "pokemon_id" : "ID своего покемона"
}

body_knockout = {
"pokemon_id": "ID своего покемона"
}

response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
print(response_create.status_code)
print(response_create.text)

response_rename = requests.put(url = f'{url}/pokemons', headers = header, json = body_rename)
print(response_rename.status_code)
print(response_rename.text)

response_catch = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_catch)
print(response_catch.status_code)
print(response_catch.text)

response_knockout = requests.post(url = f'{url}/pokemons/knockout', headers = header, json = body_knockout)
print(response_knockout.status_code)
print(response_knockout.text)


