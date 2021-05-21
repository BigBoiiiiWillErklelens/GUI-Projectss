from tkinter import *
import random
import matplotlib

top = Tk()
songList = []
myRolls = []
rollTimes = 0
dieType = 0



def addTrack ():
    songList.append(E1.get())
    E1.delete(0, END)

def printList():
    print(songList)

def exportList():
    with open("test.txt", "w") as f:
        for item in songList:
            f.write("%s/n" % item)

def clearWindow():
    for widget in top.winfo_children():
        widget.destroy()

def mainMenu():
    clearWindow()
    Lmain = Label(top, text= "Block 5 Gui Projects")
    LMain.grid(column = 0, row+1)
    
    B1Main = Button(text = , bg= , command = week1)
    B1M.grid(column = 1, row = 2)
    
    B2Main = Button(text = "Week 2". bg= "white")
    B2Main.grid(column = 1, row = 1)
                
    B3Main

def week1():
    clearWindow()
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

    B4 = Button(text = "Export", bg = "yellow", command= mainMenu)
    B4.grid(column= 0, row = 3)

def week2():
    def rollDice():
        rollTimes = E2W2.get()
        dieType = E1W2.get()

        clearWindow()

        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))

        L4W2= Label(top, text= "here are your rolls" ))
        L4W2.grid(column= 0, row= 1)
        
        L5W2= Label(top, text= "{}".format(myRolls))
        L5W2.grid(column= 0, row= 2)
        
        B2W2 = Button(text= "main menu", bg= "yellow", command = rollDice)
        B2W2.grid(column= 0, row= 3)
        
    clearWindow()

    L1W2 = Label(top, text= "Dice Roller App")
    L1W2.grid(column = 2, row = 1)

    L2W2 = Label(top, text= "# of sides")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text= "# of rolls")
    L3W2.grid(column = 3, row = 2)

    E1W2 = Entry(top, bd = 5)
    E1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column = 3, row = 3)

    B1W2 = Button(text= "Roll em", bg = "yellow"))
    B1W2.grid(column = 2, row = 4)

def downloadPlaylist():
        f.write("Now the file has more content!")
    f.close()

    
    f = open("demofile2.txt", "r")
    print(f.read())

top.mainloop()

#DunDeRmaIn
if __name__ == "__main__":
    mainProgram()
    #POO

