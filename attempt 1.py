import tkinter as tk
import os
class App(tk.Frame):
    def _init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createwidget()


master = tk.Tk()
myfortnite = App()

myfortnite.master.title("big chungus")
myfortnite.master.maxsize(1920,1080)

def readprint():
    readprint = str(input("what file do you want to read 1 , 2 , 3 ? "))
    file = open(readprint,"r")
    if file.mode == 'r':
        contents =file.read()
        print(contents)

def overwrite():
    overwrite = str(input("what file do you want to edit 1 , 2 , 3 ? "))
    write = str(input("what do you want to write? "))
    file = open(overwrite,"w")
    file.write("{}".format(write))
    print("the file now says" " {}".format(write))

def createfolder():
    os.chdir('G:\My Drive')
    foldy = str(input(" folder name: "))
    os.mkdir(foldy)
    print("Folder created called {}".format(foldy))

def createfile():
    createfile = str(input("what do you want to name the file? "))
    file = open(createfile,"w+")

def createwidget(self):
    self.chungus = tk.Button(self)
    self.chungus["text"] = "???\n(clickme)"
    self.chungus["command"] = self.chunngus
    self.chungus.pack(side="top")

    self.quit = tk.Button(self, text="QUIT", fg="red")

    self.quit.pack(side="bottom")

def chunngus(self):
    print("BIG CHUNGUS")
root = tk.Tk()
myfortnite = App(master=root)
myfortnite.mainloop()
#mank
