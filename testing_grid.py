import customtkinter

app = customtkinter.CTk()
app.geometry("600x400")

right_frame = customtkinter.CTkFrame(master=app)
right_frame.grid(row=0, column=0)

left_frame = customtkinter.CTkFrame(master=app)
left_frame.grid(row=0, column=1)




app.mainloop()