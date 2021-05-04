from tkinter import *

top = Tk()
songList = []

def addTrack ():
    songList.append(E1.get())

#this is a label widget
L1 = Label(top, text="Playlist Generator")
L1.grid(column= 0, row= 1)

#this is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row = 2)

#this is a button widget
B1 = Button(text = "Add to Playlist", bg = "white", command= addTrack)
B1.grid(column = 1, row = 2)





top.mainloop()
