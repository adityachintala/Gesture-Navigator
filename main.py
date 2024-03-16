import customtkinter
import subprocess
import json

app = customtkinter.CTk()
app.title("Gesture Navigator")
app.geometry("500x400")
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


def saveGestures():
    userDefinedControls = {}
    #      "userDefinedControls" : {
    #     "index" : "Camera",
    #     "index and middle" : "Mail",
    #     "index, middle and ring" : "Calculator",
    #     "index, middle, ring and little" : "Calendar",
    #     "thumb" : "Phone"
    #   }
    userDefinedControls["index"] = gesture1_dropdown.get()
    userDefinedControls["index and middle"] = gesture2_dropdown.get()
    userDefinedControls["index, middle and ring"] = gesture3_dropdown.get()
    userDefinedControls["index, middle, ring and little"] = gesture4_dropdown.get()
    userDefinedControls["thumb"] = gesture5_dropdown.get()
    with open("userDefinedControls.json", "w") as f:
        json.dump(userDefinedControls, f)


# First screen
menuFrame.pack(fill="both", expand=True)
launchButton = customtkinter.CTkButton(
    menuFrame, text="Launch program", command=lambda: goToExecuteProgram("new.py")
)
launchButton.pack(pady=20)
customiseButton = customtkinter.CTkButton(
    menuFrame, text="Customise gestures", command=lambda: goToCustomise()
)
customiseButton.pack(pady=20)

# Second screen
customiseDesc = customtkinter.CTkLabel(
    customiseFrame, text="Customise your gestures here"
)
customiseDesc.pack(pady=5)
customiseDesc2 = customtkinter.CTkLabel(
    customiseFrame,
    text="You have five available gestures to customise which\ncan launch an app from the given list of apps.",
)
customiseDesc2.pack(pady=5)

# Five drop down lists should be there

# Gesture 1
gesture1_frame = customtkinter.CTkFrame(customiseFrame)
gesture1_frame.pack(fill="both")

gesture1_label = customtkinter.CTkLabel(gesture1_frame, text="Gesture 1")
gesture1_label.pack(side="left", pady=5, padx=80)

gesture1_dropdown = customtkinter.CTkComboBox(gesture1_frame, values=getAppNames())
gesture1_dropdown.pack(side="left", pady=5, padx=30)
gesture1_frame.pack_configure(anchor="center")

# Gesture 2
gesture2_frame = customtkinter.CTkFrame(customiseFrame)
gesture2_frame.pack(fill="both")

gesture2_label = customtkinter.CTkLabel(gesture2_frame, text="Gesture 2")
gesture2_label.pack(side="left", pady=5, padx=80)

gesture2_dropdown = customtkinter.CTkComboBox(gesture2_frame, values=getAppNames())
gesture2_dropdown.pack(side="left", pady=5, padx=30)
gesture2_frame.pack_configure(anchor="center")

# Gesture 3
gesture3_frame = customtkinter.CTkFrame(customiseFrame)
gesture3_frame.pack(fill="both")

gesture3_label = customtkinter.CTkLabel(gesture3_frame, text="Gesture 3")
gesture3_label.pack(side="left", pady=5, padx=80)

gesture3_dropdown = customtkinter.CTkComboBox(gesture3_frame, values=getAppNames())
gesture3_dropdown.pack(side="left", pady=5, padx=30)
gesture3_frame.pack_configure(anchor="center")

# Gesture 4
gesture4_frame = customtkinter.CTkFrame(customiseFrame)
gesture4_frame.pack(fill="both")

gesture4_label = customtkinter.CTkLabel(gesture4_frame, text="Gesture 4")
gesture4_label.pack(side="left", pady=5, padx=80)

gesture4_dropdown = customtkinter.CTkComboBox(gesture4_frame, values=getAppNames())
gesture4_dropdown.pack(side="left", pady=5, padx=30)
gesture4_frame.pack_configure(anchor="center")

# Gesture 5
gesture5_frame = customtkinter.CTkFrame(customiseFrame)
gesture5_frame.pack(fill="both")

gesture5_label = customtkinter.CTkLabel(gesture5_frame, text="Gesture 5")
gesture5_label.pack(side="left", pady=5, padx=80)

gesture5_dropdown = customtkinter.CTkComboBox(gesture5_frame, values=getAppNames())
gesture5_dropdown.pack(side="left", pady=5, padx=30)
gesture5_frame.pack_configure(anchor="center")


# button to save gestures
button = customtkinter.CTkButton(
    customiseFrame, text="Save", command=lambda: saveGestures()
)
button.pack_configure(anchor="center", pady=20)


app.mainloop()
