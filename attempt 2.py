import tkinter as tk
import os
window=Tk()
class Application(tk.Frame):
    def __init__(master=None):
        tk.Frame.__init__(master)
        .pack()
        .buttoneditfile()
        .buttonreadfile()
        .buttoncreatefile()
    def buttoneditfile():
        .BEF = tk.Button()
        .BEF["text"] = "do you want to edit a file\n(click me)"
        .BEF["command"] = .overwrite
        .BEF.pack(side="top")

    def buttonreadfile():
        .BRF = tk.Button()
        .BRF["text"] = "do you want to read the file\n(click me)"
        .BRF["command"] = .readprint
        .BRF.pack(side="bottom")

    def buttoncreatefile():
        .BCF = tk.Button()
        .BCF["text"] = "do you want to create a file\n(click me)"
        .BCF["command"] = .createfile
        .BCF.pack(side="bottom")
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

root = tk.Tk()
myapp = Application(master=root)
myapp.mainloop()
