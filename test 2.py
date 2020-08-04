import os
def readprint():
    file = open("file.txt","r")
    if file.mode == 'r' :
        contents =file.read()
        print(contents)

def overwrite():
    write = str(input("what do you want to write? "))
    file = open("file.txt","w")
    file.write("{}".format(write))
    print("the file now says".format(write))

def createfolder():
    os.chdir('G:\My Drive')
    foldy = str(input(" folder name: "))
    os.mkdir(foldy)
    print("Folder created called {}".format(foldy))

def createfile():
    createfile = str(input("what do you want to name the file?"))
    file = open(createfile,"w+")

readprint()
overwrite()
readprint()
createfile()
