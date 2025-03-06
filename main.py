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


# Frames for left (Pokémon List) and right (Details)
left_frame = customtkinter.CTkFrame(app)
left_frame.grid(row=0, column=0, sticky="nsew")
left_frame.grid_propagate(False)


right_frame = customtkinter.CTkFrame(app)
right_frame.grid(row=0, column=1, sticky="nsew")
right_frame.grid_propagate(False)


# Ensure frames expand properly
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Scrollable Frame for Pokémon List
scrollable_frame = customtkinter.CTkScrollableFrame(left_frame)
scrollable_frame.pack(expand=True, fill="both", padx=10, pady=10)

def show_pokemon_details(pokemon_name):
    for widget in right_frame.winfo_children():
        widget.destroy()  # Clear previous content

    label = customtkinter.CTkLabel(right_frame, text=f"Selected: {pokemon_name}", font=("Arial", 20))
    label.pack(pady=20)

for pokemon in pokemon_list:
    button = customtkinter.CTkButton(
        scrollable_frame, 
        text=pokemon[0].capitalize(),  # Pokémon name
        command=lambda p=pokemon[0].capitalize(): show_pokemon_details(p)
    )
    button.pack(pady=5, fill="x")  # Adjust spacing & full width


app.mainloop()
