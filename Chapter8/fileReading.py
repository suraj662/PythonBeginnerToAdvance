# file = open("reprt123.txt" ,"r")
# print(file.read())
# file.close()
#
# with open("reprt123.txt" ,"r") as f:
#     data = f.read()
#     print(data)


with open("newTxtFile.txt" , "r") as f:
    #read line by line using readline
    # line1 = f.readline()
    # line2 = f.readline()
    # line3 = f.readline()
    # data = f.read()
    # print(line1)
    # print(line2)
    # print(line3)
    # print(data)
    #read all line at once
    rdLineMeth = f.readlines()
    print(rdLineMeth)


#read how many lines in notes.txt ---
with open("notes.txt" ,"r") as f1:
    listOfLines = f1.readlines()
    print(listOfLines)
    print(len(listOfLines))
