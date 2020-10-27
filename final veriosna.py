from tkinter import  *
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
        button2.place(x=89, y=150)

def overwrite():
    global text2
    text2.destroy()
    file = open(readprint,"w")
    file.write(text1.get())
    file = open(readprint,"r")
    text2=Label(window, text=file.read())
    text2.place(x=100, y=220)

def createfile():
    global text1

    createfile =str(text1.get()+".txt")
    file = open(createfile,"w+")


#tkinter features
label1=Label(window, text='File Exploring')
text2=Label(window, text=contents)
text1=Entry(bd=2)
button1 = Button(window, text='Search',command=Readprint)
button2 = Button(window, text='Edit file',command=overwrite)
button3 = Button(window, text='Create File',command=createfile)
button1.place(x=140, y=150)
text1.place(x=100, y=100)
label1.place(x=120, y=50)
text2.place(x=100, y=220)
button3.place(x=186, y=150)

#tkinter setup
window.title('File Exploring (not explorer)')
window.geometry("300x300+10+10")
canvas = Canvas(window, width=300, height=300)
img = PhotoImage(file="cock boy.gif")
canvas.create_image(150,150,image=img)
window.resizable(False, False)
window.mainloop()
