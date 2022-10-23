from pygame import mixer
from tkinter import *

root = Tk()
root.geometry("600x300")

mixer.init()

# change filename.mp3 to your file name
mixer.music.load("filename.mp3")

def pause():
    mixer.music.pause()

def play():
    mixer.music.play()

def resume():
    mixer.music.unpause()

Label(root, text="Music Player", font="lucidia 30 bold").pack()
Button(text="PLAY", command=play).place(x=200, y=100)
Button(text="PAUSE", command=pause).place(x=250, y=100)
Button(text="RESUME", command=resume).place(x=310, y=100)
Button(text="QUIT", command=quit).place(x=380, y=100)

root.mainloop()