from tkinter import *

top = Tk()
songList = []

def addTrack ():
    songList.append(E1.get())
    E1.delete(0, END)

def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s/n" % item)

#this is a label widget
L1 = Label(top, text="Our tuenes")
L1.grid(column= 0, row = 1)

#this is an entry widget
E1 = Entry(top, bd = 5)
E1.grid(column= 0, row = 2)

#this is a button widget
B1 = Button(text = " + ", bg = "white", command= addTrack)
B1.grid(column = 1, row= 2)

B2 = Button(text = "Add to Playlist", bg = "white", command= addTrack)
B2.grid(column = 1, row = 2)


B3 = Button(text="Export", bg= "4940e6", command= exportList
B3.grid(column+ 1, row= 3)




top.mainloop()
