import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2' 
token = 'USER_TRAINER_TOKEN'   
header = {'Content-Type' : 'application/json', 'trainer_token' : token}
trainer_id = 'USER_TRAINER_ID'                         
pokemon_id = 'USER_POKEMON_ID_FROM_LIST'                        
pokemon_id_2 = 'USER_POKEMON_ID_FROM_LIST_2'                       
body_create = {
    "name": "USER_RANDOM_NAME",
    "photo_id": 150
}
body_rename = {
    "pokemon_id" : "USER_POKEMON_ID_FROM_LIST",                 
     "name": "USER_RANDOM_NAME",
     "photo_id": 150
}

'''Проверка что в ответе за списком тренеров статус код 200'''
def test_status_code():
    response = requests.get(url = f'{url}/trainers')
    assert response.status_code == 200

'''Проверка что в ответе есть имя тренера'''
def test_name():
    response_name = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response_name.json()["data"][0]["trainer_name"] == 'USER_TRAINER_NAME' 

'''Проверка что в ответе есть id тренера'''
def test_id():
    response_id = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response_id.json()["data"][0]["id"] == trainer_id    

'''Проверка что в ответе уровень тренера'''
def test_level():
    response_level = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response_level.json()["data"][0]["level"] == 'USER_POKEMON_LEVEL'             
    assert response_level.status_code == 200

'''Проверка в ответе есть город тренера'''
def test_city():
    response_city = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert response_city.json()["data"][0]["city"] == 'USER_TRAINER_CITY'           
    assert response_city.status_code == 200         

'''Проверка создания нового покемона'''
def test_create_pokemon():
    response_create = requests.post(url = f'{url}/pokemons', headers = header, json = body_create)
    assert response_create.status_code == 201  

'''Проверка смены имени покемона из списка'''
def test_pokemon_rename():
    response_pokemon_rename = requests.put(url = f'{url}/pokemons', headers = header, json = body_rename)
    assert response_pokemon_rename.status_code == 200

'''Проверка что в ответе есть имя покемона из списка'''
def test_pokemon_name():
    response_pokemon_name = requests.get(url = f'{url}/pokemons', params = {'trainer_id' : trainer_id, 'pokemon_id' : pokemon_id_2})
    assert response_pokemon_name.json()["data"][0]["name"] == 'USER_POKEMON_NAME_FROM_LIST'

'''Проверка что в ответе есть информация о покемоне, видимая в карточке на сайте'''    
def test_pokemon_info():
    response_pokemon_info = requests.get(url = f'{url}/pokemons', params = {'trainer_id' : trainer_id, 'pokemon_id' : pokemon_id})
    assert response_pokemon_info.json()["data"][0]["id"] == 'USER_POKEMON_ID_FROM_LIST'     
    assert response_pokemon_info.json()["data"][0]["attack"] == 4      
    assert response_pokemon_info.json()["data"][0]["in_pokeball"] == 0 

