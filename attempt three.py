from tkinter import *
import os
class Mywindow:
    def __init__(self, win):
        self.label1=Label(win, text='Would you like to edit a text file')
        self.label2=Label(win, text='Would you like to make a new  text file')
        self.label3=Label(win, text='Would you like to read a text file')
        self.text1=Entry(bd=2)
        self.text2=Entry(bd=2)
        self.text3=Entry(bd=2)
        self.button1 = Button(win, text,'Search')
        self.text1.bind(win, command=self.editfile)
        self.text2.bind(win, command=self.newfile)
        self.text3.bind(win, command=self.readfile)




