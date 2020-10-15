from tkinter import *
import os
window=Tk()
contents=""

#functions
def Readprint():
    global readprint
    global contents
    global text2
    global text1
    error=0
    if not text1.get():
        text2=Label(window, text="please enter a file name")
        text2.place(x=100, y=220)
    else:
        text2.destroy()
        readprint = text1.get()
        while True:
            try:
                file = open(readprint,"r")
                if file.mode == 'r':
                    contents =file.read()
                    print(contents)
                    text2=Label(window, text=contents)
                    text2.place(x=100, y=220)
                break
            except:
                if error==1:
                    text2=Label(window, text="Invalid file name")
                    text2.place(x=100, y=220)
                    break
                error=error+1
                readprint=str(text1.get()+".txt")
                print(readprint)
    button2.place(x=90, y=150)

def overwrite():
    global text2
    text2.destroy()
    file = open(readprint,"w")
    file.write(text1.get())
    file = open(readprint,"r")
    text2=Label(window, text=file.read())
    text2.place(x=100, y=220)

def createfolder():
    os.chdir('G:\My Drive')
    foldy = str(input(" folder name: "))
    os.mkdir(foldy)
    print("Folder created called {}".format(foldy))

def createfile():
    createfile = str(input("what do you want to name the file? "))
    file = open(createfile,"w+")


#tkinter features
label1=Label(window, text='File Exploring ')
text2=Label(window, text=contents)
text1=Entry(bd=2)
button1 = Button(window, text='Search',command=Readprint)
button2 = Button(window, text='Edit file',command=overwrite)
button1.place(x=140, y=150)
text1.place(x=100, y=100)
label1.place(x=120, y=50)
text2.place(x=100, y=220)

#tkinter setup
window.title('file editor')
window.geometry("300x300+10+10")
window.mainloop()


