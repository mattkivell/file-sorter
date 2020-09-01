from tkinter import *
import os
class Mywindow:
    def __init__(self, win):
        self.label1=Label(win, text='What text file do you want to read')
        self.text2=Entry(bd=2)
        self.text1=Entry(bd=2)
        self.button1 = Button(win, text='Search')
        self.button1.bind('button 1', self.readprint)
        self.button1.place(x=140, y=150)
        self.text1.place(x=100, y=100)
        self.label1.place(x=80, y=50)
        self.text2.place(x=100, y=220)
    def readprint(self):
        self.text1 = str(input())
        file = open(self.text2,"r")
        if file.mode == 'r':
            contents =file.read()
            self.text2.insert(self,contents)


window=Tk()
mywin=Mywindow(window)
window.title('file editor')
window.geometry("300x300+10+10")
window.mainloop()


