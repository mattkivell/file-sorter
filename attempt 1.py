
import os
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

overwrite()
