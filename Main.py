from IO import *

def dDate(rawDate):
    dSeg = []
    fDate = ""
    if "/" in rawDate:
        dSeg = rawDate.split("/")
    elif "-" in rawDate:
        dSeg = rawDate.split("-")
    else:
        # error
        print()

    if len(dSeg) == 3:
        if not len(dSeg[0]) == 2:
            dSeg[0] = "0" + dSeg[0]

        if not len(dSeg[1]) == 2:
            dSeg[1] = "0" + dSeg[1]

        if not len(dSeg[2]) == 4:
            dSeg[2] = "20" + dSeg[2]

        fDate = dSeg[0] + dSeg[1] + dSeg[2]
        try:
            int(fDate)
        except ValueError:
            # error
            print()
    else:
        # error
        print()
    # TODO:
        # check if date is actually valid
        # fix errors to make person re-enter date


stop = False
while not stop:
    date = ""
    # read line
    currLine = readLine()

    if currLine == "stop":
        stop = True
    else:
        # output line
        writeLine(dDate(currLine))

