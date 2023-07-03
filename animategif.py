from tkinter import *
from PIL import Image, ImageTk

def animate_frames(label, frames, frame_index, window):
    frame = frames[frame_index]
    image = ImageTk.PhotoImage(frame)

    label.config(image=image)
    label.image = image

    frame_index += 1
    if frame_index >= len(frames):
        frame_index = 0

    # Schedule the next frame update (modify the delay as needed)
    window.after(100, animate_frames, label, frames, frame_index)

def load_gif_frames(path):
    # Open the GIF file
    with Image.open(path) as gif_image:
        frames = []
        try:
            while True:
                # Extract the current frame and convert it to RGB mode
                frame = gif_image.convert("RGB")
                frames.append(frame.copy())
                gif_image.seek(len(frames))  # Move to the next frame
        except EOFError:
            pass

        return frames
