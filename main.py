import customtkinter
import subprocess
import json
import uuid
import socket
import pymongo
from dotenv import load_dotenv
import os
from PIL import Image, ImageTk

class GestureAnimation:
    def __init__(self, root, anchor, gif_path):
        self.root = root
        self.gif_path = gif_path
        self.anchor = anchor

        # Load the GIF
        self.gif = Image.open(gif_path)
        self.frames = []
        self.load_frames()
        self.runFlag = True

        # Create a label to display the GIF
        self.label = customtkinter.CTkLabel(root, text="")
        self.label.pack(side=anchor, padx=20)

        # Display the GIF
        self.display_frames()

    def update_gif(self, gif_path):
        # Remove old frames
        self.runFlag = False
        self.frames.clear()

        # Load the new GIF
        self.gif = Image.open(gif_path)
        self.load_frames()
        self.runFlag = True
        self.display_frames()

    def load_frames(self):
        try:
            while True:
                self.frames.append(ImageTk.PhotoImage(self.gif.copy()))
                self.gif.seek(len(self.frames))
                print("Loaded frame")
        except EOFError:
            pass

    def display_frames(self):
        try:
            def update_frame(idx):
                if self.runFlag:
                    frame = self.frames[idx]
                    self.label.configure(image=frame)
                    self.root.after(50, update_frame, (idx + 1) % len(self.frames))

            update_frame(0)
        except Exception as e:
            pass

load_dotenv()

def get_unique_id():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    hostname = socket.gethostname()
    return f"{mac}-{hostname}"

unique_id = get_unique_id()
print(unique_id)

client = pymongo.MongoClient(os.getenv("MONGODB.URI"))

db = client["hci"]

collection = db["user-config"]

customGestureJson = collection.find_one({"_id": unique_id})

f = open("appList.json", "r")
data = json.load(f)

if customGestureJson == None:
    collection.insert_one(
        {
            "_id": unique_id,
            "name": socket.gethostname(),
            "userDefinedControls": {
                "index": "null",
                "index and middle": "null",
                "index, middle and ring": "null",
                "index, middle, ring and little": "null",
                "thumb": "null",
            },
        }
    )

    customGestureJson = collection.find_one({"_id": unique_id})

    with open("./script/modules/user_defined_data.json", "w") as f:
        json.dump(customGestureJson, f)

app = customtkinter.CTk()
app.title("Gesture Navigator")
app.geometry("500x400")
app.iconbitmap("dark.ico")

# Create two frames for the screens
menuFrame = customtkinter.CTkFrame(app)
customiseFrame = customtkinter.CTkFrame(app)
tutorialFrame = customtkinter.CTkFrame(app)

def getAppNames():
    # read a file appList.json and fetch names
    # return the list of app names
    f = open("appList.json", "r")
    data = json.load(f)
    ls = ["Select"]
    for i in data:
        ls.append(i["displayName"])
    return ls

# Function to switch to the second screen
def goToCustomise():
    menuFrame.pack_forget()
    customiseFrame.pack(fill="both", expand=True)

# Function to switch to the third screen
def goToTutorial():
    menuFrame.pack_forget()
    tutorialFrame.pack(fill="both", expand=True)

# Function to run python script
def launchGestureControl():
    print("Hello World")
    subprocess.Popen(["python", "script/modules/anotherimport.py"])

# Function to switch back to the first screen
def backToMenuFrame():
    customiseFrame.pack_forget()
    menuFrame.pack(fill="both", expand=True)

# Function to print "Hello, World!"
def print_hello_world(varName):
    print("Hello, World!", varName)

def saveGestures(data):
    userDefinedControls = {}
    userDefinedControls["index"] = (
        gesture1_dropdown.get() if gesture1_dropdown.get() != "Select" else "null"
    )
    userDefinedControls["index and middle"] = (
        gesture2_dropdown.get() if gesture2_dropdown.get() != "Select" else "null"
    )
    userDefinedControls["index, middle and ring"] = (
        gesture3_dropdown.get() if gesture3_dropdown.get() != "Select" else "null"
    )
    userDefinedControls["index, middle, ring and little"] = (
        gesture4_dropdown.get() if gesture4_dropdown.get() != "Select" else "null"
    )
    userDefinedControls["thumb"] = (
        gesture5_dropdown.get() if gesture5_dropdown.get() != "Select" else "null"
    )

    for i in data:
        if i["displayName"] == userDefinedControls["index"]:
            userDefinedControls["index"] = i["shellName"]
        if i["displayName"] == userDefinedControls["index and middle"]:
            userDefinedControls["index and middle"] = i["shellName"]
        if i["displayName"] == userDefinedControls["index, middle and ring"]:
            userDefinedControls["index, middle and ring"] = i["shellName"]
        if i["displayName"] == userDefinedControls["index, middle, ring and little"]:
            userDefinedControls["index, middle, ring and little"] = i["shellName"]
        if i["displayName"] == userDefinedControls["thumb"]:
            userDefinedControls["thumb"] = i["shellName"]

    if customGestureJson is not None:
        customGestureJson["userDefinedControls"] = userDefinedControls
        collection.update_one({"_id": unique_id}, {"$set": customGestureJson})

    with open("./script/modules/user_defined_data.json", "w") as f:
        json.dump(customGestureJson, f)

# First screen
menuFrame.pack(fill="both", expand=True)
launchButton = customtkinter.CTkButton(
    menuFrame, text="Launch program", command=lambda: launchGestureControl(),
)
launchButton.pack(pady=60)

customiseButton = customtkinter.CTkButton(
    menuFrame, text="Customise gestures", command=lambda: goToCustomise()
)
customiseButton.pack(pady=30)

tutorialButton = customtkinter.CTkButton(
    menuFrame, text="Tutorial", command=lambda: goToTutorial()
)
tutorialButton.pack(pady=60)

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
if customGestureJson is not None:
    for i in data:
        if i["shellName"] == customGestureJson["userDefinedControls"]["index"]:
            gesture1_dropdown.set(i["displayName"])
gesture1_frame.pack_configure(anchor="center")

# Gesture 2
gesture2_frame = customtkinter.CTkFrame(customiseFrame)
gesture2_frame.pack(fill="both")

gesture2_label = customtkinter.CTkLabel(gesture2_frame, text="Gesture 2")
gesture2_label.pack(side="left", pady=5, padx=80)

gesture2_dropdown = customtkinter.CTkComboBox(gesture2_frame, values=getAppNames())
gesture2_dropdown.pack(side="left", pady=5, padx=30)
if customGestureJson is not None:
    for i in data:
        if i["shellName"] == customGestureJson["userDefinedControls"]["index and middle"]:
            gesture2_dropdown.set(i["displayName"])
gesture2_frame.pack_configure(anchor="center")

# Gesture 3
gesture3_frame = customtkinter.CTkFrame(customiseFrame)
gesture3_frame.pack(fill="both")

gesture3_label = customtkinter.CTkLabel(gesture3_frame, text="Gesture 3")
gesture3_label.pack(side="left", pady=5, padx=80)

gesture3_dropdown = customtkinter.CTkComboBox(gesture3_frame, values=getAppNames())
gesture3_dropdown.pack(side="left", pady=5, padx=30)
if customGestureJson is not None:
    for i in data:
        if i["shellName"] == customGestureJson["userDefinedControls"]["index, middle and ring"]:
            gesture3_dropdown.set(i["displayName"])
gesture3_frame.pack_configure(anchor="center")

# Gesture 4
gesture4_frame = customtkinter.CTkFrame(customiseFrame)
gesture4_frame.pack(fill="both")

gesture4_label = customtkinter.CTkLabel(gesture4_frame, text="Gesture 4")
gesture4_label.pack(side="left", pady=5, padx=80)

gesture4_dropdown = customtkinter.CTkComboBox(gesture4_frame, values=getAppNames())
gesture4_dropdown.pack(side="left", pady=5, padx=30)
if customGestureJson is not None:
    for i in data:
        if i["shellName"] == customGestureJson["userDefinedControls"]["index, middle, ring and little"]:
            gesture4_dropdown.set(i["displayName"])
gesture4_frame.pack_configure(anchor="center")

# Gesture 5
gesture5_frame = customtkinter.CTkFrame(customiseFrame)
gesture5_frame.pack(fill="both")

gesture5_label = customtkinter.CTkLabel(gesture5_frame, text="Gesture 5")
gesture5_label.pack(side="left", pady=5, padx=80)

gesture5_dropdown = customtkinter.CTkComboBox(gesture5_frame, values=getAppNames())
gesture5_dropdown.pack(side="left", pady=5, padx=30)
if customGestureJson is not None:
    for i in data:
        if i["shellName"] == customGestureJson["userDefinedControls"]["thumb"]:
            gesture5_dropdown.set(i["displayName"])
gesture5_frame.pack_configure(anchor="center")


# button to save gestures
saveButton = customtkinter.CTkButton(
    customiseFrame, text="Save", command=lambda: saveGestures(data)
)
saveButton.pack_configure(anchor="center", pady=20)
backToMainMenu = customtkinter.CTkButton(
    customiseFrame, text="Back", command=lambda: backToMenuFrame()
)
backToMainMenu.pack_configure(anchor="center", pady=20)

# Third Screen
# Third screen is for the user to view tutorial

# Define the paths for the GIFs
gif_info = {
    "Option 1": {"left": "1.gif", "right": "2.gif", "description": "This is a description for option 1."},
    "Option 2": {"left": "3.gif", "right": "4.gif", "description": "This is a description for option 2."},
    "Option 3": {"left": "5.gif", "right": "6.gif", "description": "This is a description for option 3."}
}

# Create a dropdown list
options = list(gif_info.keys())
selected_option = customtkinter.StringVar()
dropdown = customtkinter.CTkComboBox(tutorialFrame, values=options, variable=selected_option)
dropdown.set(options[0])
dropdown.pack(pady=20)

# Create a frame for the GIFs
gif_frame = customtkinter.CTkFrame(tutorialFrame)
gif_frame.pack(pady=10)

# Create labels for the GIFs
left_gif_label = GestureAnimation(gif_frame, "left", "1.gif")
right_gif_label = GestureAnimation(gif_frame, "right", "2.gif")

# Create a frame for the heading and description
description_frame = customtkinter.CTkFrame(tutorialFrame)
description_frame.pack(pady=20)

# Create the heading
heading = customtkinter.CTkLabel(description_frame, text="Description", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Create the description text
description_label = customtkinter.CTkLabel(description_frame, text=gif_info["Option 1"]["description"], wraplength=600)
description_label.pack()

# Function to update the GIFs based on the selected option
def update_gifs(*_):
    option = selected_option.get()
    left_gif_path = gif_info[option]["left"]
    right_gif_path = gif_info[option]["right"]

    left_gif_label.update_gif(left_gif_path)
    right_gif_label.update_gif(right_gif_path)
    description_label.configure(text=gif_info[option]["description"])

# Bind the update_gifs function to the dropdown selection
selected_option.trace_add("write", update_gifs)

# Create a button to go back to the main menu
back_button = customtkinter.CTkButton(tutorialFrame, text="Back", command=backToMenuFrame)
back_button.pack(pady=20)

app.mainloop()