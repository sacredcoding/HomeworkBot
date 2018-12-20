from IO import *
from Verif import *

stop = False
while not stop:
    date = ""
    # read line
    currLine = readLine()

    if currLine == "stop":
        stop = True
    else:
        date = dDate(currLine)
        if date == -1:
            print("Re-enter your date plz mm-dd-yyyy")
            continue
        else:
            print(date)

