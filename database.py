import sqlite3
import requests


# SQLite connection and cursor
conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()


'''class Pokemon:
    def __init__(self, pokemon_id):
        self.pokemon_id = pokemon_id
        self.name = None

    def fetch_pokemon_data(self):
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(f"{base_url}{self.pokemon_id}")

        if response.status_code == 200:
            data = response.json()
            self.name = data['name']  
            return self.name.capitalize()
        else:
            print(f"Failed to retrieve data for Pokemon with ID {self.pokemon_id}")
            return None
        
for i in range(152):
    pokemon = Pokemon(i)
    pokemon_name = pokemon.fetch_pokemon_data()  
    if pokemon_name: 
        cursor.execute("""
            UPDATE pokemon
            SET name = :name
            WHERE id = :id""", {'id':i, 'name':pokemon_name})'''


'''# Schema for creating the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Inserting Pokémon data
for i in range(1, 152):  
    pokemon = Pokemon(i)
    pokemon_name = pokemon.fetch_pokemon_data()  
    if pokemon_name:  
        cursor.execute("""
            INSERT INTO pokemon (id, name)
            VALUES (:id, :name)
        """, {'id': i, 'name': pokemon_name})

'''
'''cursor.execute("""
    SELECT *
    FROM pokemon
""")


print(cursor.fetchall())

'''

'''# Table which includes sprite and info of pokemon
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon_info (
        pokemon_id,
        sprite TEXT NOT NULL,
        info_text TEXT NOT NULL,
        FOREIGN KEY (pokemon_id) REFERENCES pokemon(id)
    )
""")'''

## FETCHING FLAVOR TEXT FOR POKEMON ##

def fetch_pokemon_flavor_text(pokemon_id):
    base_url = "https://pokeapi.co/api/v2/pokemon-species/"
    response = requests.get(f"{base_url}{pokemon_id}")

    if response.status_code == 200:
        data = response.json()

        for entry in data ["flavor_text_entries"]:
            if entry ["language"]["name"] == "en" and entry["version"]["name"] == "red":
                return entry["flavor_text"].replace("\n", " ").replace("\f", " ")
          
        
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None


## FETCH POKEMON SPRITE ##

def fetch_pokemon_sprite(pokemon_id):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(f"{base_url}{pokemon_id}")

    
    if response.status_code == 200:
        data = response.json()
        sprite_url = data["sprites"]["other"]["official-artwork"]["front_default"]
        return sprite_url
    
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None

        
for i in range(1, 152):
    pokemon_art = fetch_pokemon_sprite(i)
    pokemon_flavor = fetch_pokemon_flavor_text(i)

    cursor.execute("""
        INSERT INTO pokemon_info(pokemon_id, sprite, info_text)
        VALUES
        (:id, :art, :text)
""", {'id':i, 'art':pokemon_art, 'text':pokemon_flavor}
)


conn.commit()
conn.close()