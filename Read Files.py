def readprint():
    file = open("file.txt","r")
    if file.mode == 'r' :
        contents =file.read()
        print(contents)
readprint()
