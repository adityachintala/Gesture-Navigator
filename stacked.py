import tkinter as tk
from PIL import Image, ImageTk

def display_gif(root, gif_paths):
    def load_frames(gif_path):
        gif = Image.open(gif_path)
        frames = []
        try:
            while True:
                frames.append(ImageTk.PhotoImage(gif.copy()))
                gif.seek(len(frames))
        except EOFError:
            pass
        return frames

    frames_left = load_frames(gif_paths[0])
    frames_right = load_frames(gif_paths[1])

    # Create labels for left and right hands
    label_left = tk.Label(root, text="Left Hand")
    label_left.grid(row=0, column=0, padx=10)
    label_right = tk.Label(root, text="Right Hand")
    label_right.grid(row=0, column=1, padx=10)

    # Create labels for displaying GIFs
    label_left_gif = tk.Label(root)
    label_left_gif.grid(row=1, column=0)
    label_right_gif = tk.Label(root)
    label_right_gif.grid(row=1, column=1)

    def update_frame_left(idx=0):
        label_left_gif.config(image=frames_left[idx])
        idx = (idx + 1) % len(frames_left)
        root.after(100, update_frame_left, idx)

    def update_frame_right(idx=0):
        label_right_gif.config(image=frames_right[idx])
        idx = (idx + 1) % len(frames_right)
        root.after(100, update_frame_right, idx)

    update_frame_left()
    update_frame_right()

if __name__ == "__main__":
    root = tk.Tk()
    gif_paths = ["1.gif", "2.gif"]  # List of paths to your GIFs
    display_gif(root, gif_paths)
    root.mainloop()
