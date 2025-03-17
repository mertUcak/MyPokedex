import sqlite3
import requests
import customtkinter
from PIL import Image
import io

conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM pokemon ORDER BY id ASC")
pokemon_list = cursor.fetchall()

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
app.title("MyPokedex")
app.geometry("800x600")
app.resizable(True, True)

app.grid_rowconfigure(0, weight=1, uniform="equal")
app.grid_columnconfigure(0, weight=1, uniform="equal")
app.grid_columnconfigure(1, weight=1, uniform="equal")

left_scrool_frame = customtkinter.CTkScrollableFrame(master=app)
left_scrool_frame.grid(row=0, column=0, padx=(20, 10), pady=(20), sticky="nsew")
left_scrool_frame.grid_columnconfigure(0, weight=1)

right_info_frame = customtkinter.CTkFrame(master=app)
right_info_frame.grid(row=0, column=1, padx=(10, 20), pady=(20), sticky="nsew")
right_info_frame.grid_columnconfigure(0, weight=1)
right_info_frame.grid_rowconfigure(0, weight=1)
right_info_frame.grid_rowconfigure(1, weight=1)
right_info_frame.grid_rowconfigure(2, weight=3)

##pokemon_label_name = customtkinter.CTkLabel(master=right_info_frame, text="Charmander", font=("Arial", 16, "bold"))
##pokemon_label_name.grid(column=0, row=0)

##pokemon_image = Image.open(requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png", stream=True).raw)
##pokemon_sprite = customtkinter.CTkImage(light_image=pokemon_image, dark_image=pokemon_image, size=(300,300))
##pokemon_label_sprite = customtkinter.CTkLabel(master=right_info_frame, text="", image=pokemon_sprite)
##pokemon_label_sprite.grid(column=0, row=1)

##pokemon_label_flavor = customtkinter.CTkLabel(master=right_info_frame, text="Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.", wraplength=350)
##pokemon_label_flavor.grid(column=0, row=2, sticky="nsew")

pokemon_label_name = customtkinter.CTkLabel(master=right_info_frame, text="", font=("Arial", 16, "bold"))
pokemon_label_name.grid(column=0, row=0)

pokemon_label_sprite = customtkinter.CTkLabel(master=right_info_frame, text="", image=None)
pokemon_label_sprite.grid(column=0, row=1)

pokemon_label_flavor = customtkinter.CTkLabel(master=right_info_frame, text="", wraplength=350)
pokemon_label_flavor.grid(column=0, row=2, sticky="nsew")

import io

def update_pokemon(pokemon_id):
    cursor.execute("SELECT name FROM pokemon WHERE id=?", (pokemon_id,))
    pokemon_name = cursor.fetchone()[0]

    cursor.execute("SELECT sprite, info_text FROM pokemon_info WHERE pokemon_id=?", (pokemon_id,))
    pokemon_info = cursor.fetchone()

    if pokemon_info:
        sprite_link, flavor_text = pokemon_info
        response = requests.get(sprite_link)
        
        im = Image.open(io.BytesIO(response.content))
        pokemon_sprite = customtkinter.CTkImage(light_image=im, dark_image=im, size=(300,300))
        pokemon_label_sprite.configure(image=pokemon_sprite)  
        pokemon_label_name.configure(text=pokemon_name)  
        pokemon_label_flavor.configure(text=flavor_text)

for pokemon_id, pokemon in enumerate(pokemon_list, start=1):
    pokemon_name = pokemon[0].capitalize()

    button = customtkinter.CTkButton(
        master=left_scrool_frame,
        text=pokemon_name,
        command=lambda id=pokemon_id: update_pokemon(id)  
    )
    button.grid(column=0, padx=(30), pady=(5), sticky="ew")

app.mainloop()
conn.close()