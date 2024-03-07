import customtkinter as tk

tk.set_appearance_mode("Dark")
tk.set_default_color_theme("blue")

app = tk.CTk()
app.geometry("800x600")
app.title("Gesture Navigator")

print(tk.get_appearance_mode())
app.iconbitmap("dark.ico")

# Create a label with initial transparency set to 0
label = tk.CTkLabel(app, text="Welcome\nto\nGesture Navigator!", height=5, width=20, font=("Clarendon", 50), text_color="white")
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

app.after(2000, lambda: label.configure(text="Hello World!"))

app.mainloop()