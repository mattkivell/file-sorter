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

readprint()
overwrite()
readprint()
