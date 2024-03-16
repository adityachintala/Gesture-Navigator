import customtkinter
import subprocess
import json

app = customtkinter.CTk()
app.title("Gesture Navigator")
app.geometry("500x300")
app.iconbitmap("dark.ico")

# Create two frames for the screens
menuFrame = customtkinter.CTkFrame(app)
customiseFrame = customtkinter.CTkFrame(app)

def getAppNames():
    # read a file appList.json and fetch names
    # return the list of app names
    f = open("appList.json", "r")
    data = json.load(f)
    ls = []
    for i in data:
        ls.append(i["displayName"])
    return ls


# Function to switch to the second screen
def goToCustomise():
    menuFrame.pack_forget()
    customiseFrame.pack(fill="both", expand=True)

# Function to run python script
def goToExecuteProgram(filePath):
    print("Starting Program")
    subprocess.run(["python", filePath])

# Function to switch back to the first screen
def backToMenuFrame():
    customiseFrame.pack_forget()
    menuFrame.pack(fill="both", expand=True)

# Function to print "Hello, World!"
def print_hello_world(varName):
    print("Hello, World!", varName)

# First screen
menuFrame.pack(fill="both", expand=True)
launchButton = customtkinter.CTkButton(menuFrame, text="Launch program", command=lambda:goToExecuteProgram("new.py"))
launchButton.pack(pady=20)
customiseButton = customtkinter.CTkButton(menuFrame, text="Customise gestures", command=lambda:goToCustomise())
customiseButton.pack(pady=20)

# Second screen
customiseDesc = customtkinter.CTkLabel(customiseFrame, text="Customise your gestures here")
customiseDesc.pack(pady=5)
customiseDesc2 = customtkinter.CTkLabel(customiseFrame, text="You have five available gestures to customise which can launch an app from the given list of apps.")
customiseDesc2.pack(pady=5)

# Five drop down lists should be there

# Gesture 1
gesture1 = customtkinter.CTkLabel(customiseFrame, text="Gesture 1")
gesture1Text = customtkinter.StringVar(value="option 2")  # set initial value
gesture1.pack(pady=20)
gesture1_dropdown = customtkinter.CTkComboBox(customiseFrame, values=getAppNames(), variable=gesture1Text)
gesture1_dropdown.pack(pady=20)


app.mainloop()