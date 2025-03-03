import requests
import sqlite3
import json

########## EXTRACTING POKEMON INFORMATION FROM API ##########

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(id):
    url = f"{base_url}/pokemon/{id}"
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Failed to retrieve data {response.status_code}")

'''pokemon_info = get_pokemon_info(4)

if pokemon_info:
    print(f"{pokemon_info["name"]}")'''



########## INSERTING DATA INTO SQL DATABASE ##########

conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")


conn.commit()
conn.close()