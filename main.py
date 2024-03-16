import customtkinter

app = customtkinter.CTk()
app.title("Gesture Navigator")
app.geometry("500x300")
app.iconbitmap("dark.ico")

# Create two frames for the screens
menuFrame = customtkinter.CTkFrame(app)
customiseFrame = customtkinter.CTkFrame(app)

# Function to switch to the second screen
def goToCustomise():
    menuFrame.pack_forget()
    customiseFrame.pack(fill="both", expand=True)

# Function to switch back to the first screen
def backToMenuFrame():
    customiseFrame.pack_forget()
    menuFrame.pack(fill="both", expand=True)

# Function to print "Hello, World!"
def print_hello_world():
    print("Hello, World!")

# First screen
menuFrame.pack(fill="both", expand=True)
button_1 = customtkinter.CTkButton(menuFrame, text="Launch program", command=goToCustomise)
button_1.pack(pady=20)
button_1 = customtkinter.CTkButton(menuFrame, text="Customise gestures", command=goToCustomise)
button_1.pack(pady=20)

# Second screen
button_2 = customtkinter.CTkButton(customiseFrame, text="Back to Screen 1", command=backToMenuFrame)
button_2.pack(pady=20)
button_3 = customtkinter.CTkButton(customiseFrame, text="Print Hello, World!", command=print_hello_world)
button_3.pack(pady=20)

app.mainloop()