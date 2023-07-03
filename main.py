from tkinter import *
from PIL import Image, ImageTk

remote = Tk()
remote.title("TV Remote")
remote.geometry("225x250")
channelFileArray = ["rainforest.gif", "rainforest2.gif", "BBC.gif", "nat.gif","geosuper.gif","tvanouvelle.jpg","nickgif.gif","cartoonetwork.gif"]
channelIndex = 0
gif_labels = []

def animate_frames(label, frames, frame_index):
    frame = frames[frame_index]
    image = ImageTk.PhotoImage(frame)

    label.config(image=image)
    label.image = image

    frame_index += 1
    if frame_index >= len(frames):
        frame_index = 0

    # Schedule the next frame update (modify the delay as needed)
    remote.after(150, animate_frames, label, frames, frame_index)

def load_gif_frames(path):
    frames = []
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

def changeChannelUP():
    global channelIndex
    channelIndex += 1
    print(channelIndex)
    try:
        gif_frames = load_gif_frames(channelFileArray[channelIndex])
        animate_frames(gif_labels[channelIndex], gif_frames, 0)
        gif_labels[channelIndex].pack()
        gif_labels[channelIndex - 1].pack_forget()
    except IndexError:
        gif_frames = load_gif_frames(channelFileArray[channelIndex - 1])
        animate_frames(gif_labels[channelIndex - 1], gif_frames, 0)

def changeChannelDOWN():
    global channelIndex
    if channelIndex == 0:  # If currently on the first channel
        channelIndex = len(channelFileArray) - 1  # Switch to the last channel
        gif_frames = load_gif_frames(channelFileArray[channelIndex])
        animate_frames(gif_labels[channelIndex], gif_frames, 0)
        gif_labels[channelIndex].pack()
        gif_labels[0].pack_forget()
    else:
        channelIndex -= 1
        print(channelIndex)
        gif_frames = load_gif_frames(channelFileArray[channelIndex])
        animate_frames(gif_labels[channelIndex], gif_frames, 0)
        gif_labels[channelIndex].pack()
        gif_labels[channelIndex + 1].pack_forget()



def turnOnTV():
    '''callback method used for turn_on button'''
    # use a Toplevel widget to display an image in a new window
    window = Toplevel(remote)
    window.title("TV")

    for i in range(len(channelFileArray)):
        gif_frames = load_gif_frames(channelFileArray[i])
        label = Label(window)
        label.pack()
        animate_frames(label, gif_frames, 0)
        gif_labels.append(label)
    gif_labels[0].pack()

def turnOffTV():
    remote.destroy()
    print("destroyed")

# create buttons and label for remote
controlLabel = Label(remote, text="CONTROLS")
onButton = Button(remote, text="ON", command=turnOnTV)
offButton = Button(remote, text="OFF", command=turnOffTV)
volumeLabel = Label(remote, text="VOLUME")
volup = Button(remote, text="+")
voldown = Button(remote, text="-")
channelLabel = Label(remote, text="CHANNEL")
chanUp = Button(remote, text="↑", command=changeChannelUP)
chanDown = Button(remote, text="↓", command=changeChannelDOWN)

# pack elements to remote
controlLabel.pack()
onButton.pack()
offButton.pack()
volumeLabel.pack()
volup.pack()
voldown.pack()
channelLabel.pack()
chanUp.pack()
chanDown.pack()

# open window
remote.mainloop()
