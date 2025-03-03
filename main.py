import sqlite3
import requests
import tkinter as tk

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


'''# SQLite connection and cursor
conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()'''

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


conn.commit()
conn.close()'''


class Application(tk.Frame):              
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)   
        self.grid(column=2, row=5, padx=20, pady=20)                           

app = Application()                       
app.master.title('Sample application')    
app.mainloop()      