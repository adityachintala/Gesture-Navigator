import customtkinter as ctk
from PIL import Image, ImageTk

# Create the main window
root = ctk.CTk()
root.title("My GUI")
root.after(0, lambda: root.focus_force())

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
        self.label = ctk.CTkLabel(root, text="")
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
                frame = self.frames[idx]
                self.label.configure(image=frame)
                if self.runFlag:
                    self.root.after(30, update_frame, (idx + 1) % len(self.frames))

            update_frame(0)
        except Exception as e:
            pass

# Define the paths for the GIFs
gif_paths = {
    "Option 1": {"left": "1.gif", "right": "2.gif"},
    "Option 2": {"left": "3.gif", "right": "4.gif"},
    "Option 3": {"left": "5.gif", "right": "6.gif"}
}

# Create a dropdown list
options = list(gif_paths.keys())
selected_option = ctk.StringVar()
dropdown = ctk.CTkComboBox(root, values=options, variable=selected_option)
dropdown.set(options[0])
dropdown.pack(pady=20)

# Create a frame for the GIFs
gif_frame = ctk.CTkFrame(root)
gif_frame.pack(pady=10)

# Create labels for the GIFs
left_gif_label = GestureAnimation(gif_frame, "left", "1.gif")
right_gif_label = GestureAnimation(gif_frame, "right", "2.gif")

# Create a frame for the heading and description
description_frame = ctk.CTkFrame(root)
description_frame.pack(pady=20)

# Create the heading
heading = ctk.CTkLabel(description_frame, text="Description", font=("Arial", 16, "bold"))
heading.pack(pady=10)

# Create the description text
description_text = "This is a small description."
description_label = ctk.CTkLabel(description_frame, text=description_text, wraplength=600)
description_label.pack()

# Function to update the GIFs based on the selected option
def update_gifs(*_):
    option = selected_option.get()
    left_gif_path = gif_paths[option]["left"]
    right_gif_path = gif_paths[option]["right"]

    left_gif_label.update_gif(left_gif_path)
    right_gif_label.update_gif(right_gif_path)

# Bind the update_gifs function to the dropdown selection
selected_option.trace_add("write", update_gifs)

# Run the main loop
root.mainloop()