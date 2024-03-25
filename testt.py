from tkinter import *
import customtkinter as ctk  # Import customTkinter
from PIL import Image, ImageTk  # Import Pillow for image processing

# Define GIF paths and image variables
gif_paths = ["1.gif", "2.gif"]  # Replace with your GIF paths
images = []  # Initialize empty image variables

# Create a customTkinter window
root = ctk.CTk()
root.geometry("500x300")  # Set initial window size

# Initialize the images list with None values
images = [None] * len(gif_paths)

# Load GIFs (outside the function for efficiency)
for i, path in enumerate(gif_paths):
    images[i] = ImageTk.PhotoImage(Image.open(path))

# Create customTkinter label to display GIF
label = ctk.CTkLabel(root)
label.pack()

# Current GIF index (starts with first GIF)
current_gif_index = 0

# Define a function to change and display the GIF
def change_gif():
    global current_gif_index
    current_gif_index = (current_gif_index + 1) % len(gif_paths)  # Wrap around
    label.configure(image=images[current_gif_index])

# Create and configure a customTkinter button
button = ctk.CTkButton(root, text="Change GIF", command=change_gif)
button.pack()

# Run the mainloop
root.mainloop()
