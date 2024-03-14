import customtkinter

customtkinter.set_appearance_mode("system")

app = customtkinter.CTk()
app.geometry("800x600")

button = customtkinter.CTkButton(app, text="Hello World!")
button.pack()

app.mainloop()