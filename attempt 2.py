import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.chungus = tk.Button(self)
        self.chungus["text"] = "idk what to write\n(click me)"
        self.chungus["command"] = self.overwrite
        self.chungus.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def readprint(self):
        readprint = str(input("what file do you want to read 1 , 2 , 3 ? "))
        file = open(readprint,"r")
        if file.mode == 'r':
            contents =file.read()
            print(contents)

    def overwrite(self):
        overwrite = str(input("what file do you want to edit 1 , 2 , 3 ? "))
        write = str(input("what do you want to write? "))
        file = open(overwrite,"w")
        file.write("{}".format(write))
        print("the file now says" " {}".format(write))

    def createfolder(self):
        os.chdir('G:\My Drive')
        foldy = str(input(" folder name: "))
        os.mkdir(foldy)
        print("Folder created called {}".format(foldy))

    def createfile(self):
        createfile = str(input("what do you want to name the file? "))
        file = open(createfile,"w+")

root = tk.Tk()
myapp = Application(master=root)
myapp.mainloop()
myapp.master.title("things")
myapp.master.maxsize(1080,1920)
