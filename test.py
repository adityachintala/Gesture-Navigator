import customtkinter
from PIL import Image, ImageTk

app = customtkinter.CTk()
app.title("Screen Navigation Example")

# Create two frames for the screens
frame_1 = customtkinter.CTkFrame(app)
frame_2 = customtkinter.CTkFrame(app)

# Load the GIF
gif_file = "your_gif_file.gif"  # Replace with the path to your GIF file
gif = Image.open(gif_file)
frames = []

try:
    for i in range(gif.n_frames):
        gif.seek(i)
        frames.append(ImageTk.PhotoImage(gif))
except Exception as e:
    print(f"Error loading GIF: {e}")

# Function to switch to the second screen
def switch_to_screen_2():
    frame_1.pack_forget()
    frame_2.pack(fill="both", expand=True)

# Function to switch back to the first screen
def switch_to_screen_1():
    frame_2.pack_forget()
    frame_1.pack(fill="both", expand=True)

# Function to print "Hello, World!"
def print_hello_world():
    print("Hello, World!")

# First screen
frame_1.pack(fill="both", expand=True)
button_1 = customtkinter.CTkButton(frame_1, text="Go to Screen 2", command=switch_to_screen_2)
button_1.pack(pady=20)

# Second screen
frame_2.pack(fill="both", expand=True)
button_2 = customtkinter.CTkButton(frame_2, text="Back to Screen 1", command=switch_to_screen_1)
button_2.pack(pady=20)
button_3 = customtkinter.CTkButton(frame_2, text="Print Hello, World!", command=print_hello_world)
button_3.pack(pady=20)

# Add the GIF to the second screen
gif_label = customtkinter.CTkLabel(frame_2)
gif_label.pack(pady=20)

def update_gif(idx):
    frame = frames[idx]
    idx += 1
    gif_label.configure(image=frame)
    gif_label.after(50, update_gif, idx % len(frames))

update_gif(0)

app.mainloop()