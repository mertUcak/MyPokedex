import sqlite3
import requests

class Pokemon:
    def __init__(self, pokemon_id):
        self.pokemon_id = pokemon_id
        self.name = None

    def fetch_pokemon_data(self):
        base_url = "https://pokeapi.co/api/v2/pokemon/"
        response = requests.get(f"{base_url}{self.pokemon_id}")

        if response.status_code == 200:
            data = response.json()
            self.name = data['name']  # Extract the Pokémon's name
            return self.name
        else:
            print(f"Failed to retrieve data for Pokémon with ID {self.pokemon_id}")
            return None


# SQLite connection and cursor
conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()

# Schema for creating the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")

# Inserting Pokémon data
for i in range(1, 152):  # Pokémon IDs are 1 to 151
    pokemon = Pokemon(i)
    pokemon_name = pokemon.fetch_pokemon_data()  # Fetch name for each Pokémon
    if pokemon_name:  # Only insert if the name was successfully fetched
        cursor.execute("""
            INSERT INTO pokemon (id, name)
            VALUES (:id, :name)
        """, {'id': i, 'name': pokemon_name})

# Verifying the inserted data
cursor.execute("""
    SELECT *
    FROM pokemon
""")

# Printing the inserted Pokémon data
print(cursor.fetchall())

# Committing the changes and closing the connection
conn.commit()
conn.close()
