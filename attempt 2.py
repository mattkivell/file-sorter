import tkinter as tk
import os
class Application(tk.Frame):
    def __init__(penis, master=None):
        tk.Frame.__init__(penis, master)
        penis.pack()
        penis.buttoneditfile()
        penis.buttonreadfile()
        penis.buttoncreatefile()
    def buttoneditfile(penis):
        penis.BEF = tk.Button(penis)
        penis.BEF["text"] = "do you want to edit a file\n(click me)"
        penis.BEF["command"] = penis.overwrite
        penis.BEF.pack(side="top")

    def buttonreadfile(penis):
        penis.BRF = tk.Button(penis)
        penis.BRF["text"] = "do you want to read the file\n(click me)"
        penis.BRF["command"] = penis.readprint
        penis.BRF.pack(side="bottom")

    def buttoncreatefile(penis):
        penis.BCF = tk.Button(penis)
        penis.BCF["text"] = "do you want to create a file\n(click me)"
        penis.BCF["command"] = penis.createfile
        penis.BCF.pack(side="bottom")
    def readprint(penis):
        readprint = str(input("what file do you want to read 1 , 2 , 3 ? "))
        file = open(readprint,"r")
        if file.mode == 'r':
            contents =file.read()
            print(contents)

    def overwrite(penis):
        overwrite = str(input("what file do you want to edit 1 , 2 , 3 ? "))
        write = str(input("what do you want to write? "))
        file = open(overwrite,"w")
        file.write("{}".format(write))
        print("the file now says" " {}".format(write))

    def createfolder(penis):
        os.chdir('G:\My Drive')
        foldy = str(input(" folder name: "))
        os.mkdir(foldy)
        print("Folder created called {}".format(foldy))

    def createfile(penis):
        createfile = str(input("what do you want to name the file? "))
        file = open(createfile,"w+")

root = tk.Tk()
myapp = Application(master=root)
myapp.mainloop()
