import sqlite3
import requests
import customtkinter


conn = sqlite3.connect("pokedex.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM pokemon ORDER BY id ASC")
pokemon_list = cursor.fetchall()
conn.close()

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

for pokemon in pokemon_list:
    pokemon_name = pokemon[0].capitalize()

    button = customtkinter.CTkButton(master=left_scrool_frame, text=pokemon_name)
    button.grid(column=0, padx=(30), pady=(5), sticky="ew")



app.mainloop()
