def dDate(rawDate):
    # unnecessary but good practice when using a language other than Python
    # array that holds our split up date
    dSeg = []
    # string that we will return to the main loop containing the final date in a format the computer can understand
    fDate = ""

    # check if contains proper formatting
    if "/" in rawDate:
        dSeg = rawDate.split("/")
    elif "-" in rawDate:
        dSeg = rawDate.split("-")
    else:
        # error
        return -1

    # check if correct length
    if len(dSeg) == 3:
        # make sure that every part of the date is 2-2-4 (d-m-y) characters long so that the returned value is 8 characters
        # variables for the length of m, d, y, respectively
        lM = len(dSeg[0])
        lD = len(dSeg[1])
        lY = len(dSeg[2])

        if lM == 1:
            dSeg[0] = "0" + dSeg[0]
        elif not (lM == 2):
            # error
            return -1

        if lD == 1:
            dSeg[1] = "0" + dSeg[1]
        elif not (lD == 2):
            # error
            return -1

        if lY == 2:
            dSeg[2] = "20" + dSeg[2]
        elif not (lY == 4):
            # error
            return -1
    else:
        # error
        return -1

    # check if int by setting fDate and trying to turn it into an int
    # if fDate cannot be turned into an int, then it will give an error, which is what the except ValueError handles
    fDate = dSeg[0] + dSeg[1] + dSeg[2]
    try:
        int(fDate)
    except ValueError:
        # error
        return -1

    # know that dSeg[n] can be turned into an integer from condition above
    m = int(dSeg[0])
    d = int(dSeg[1])
    y = int(dSeg[2])

    # months with 30 days: 4, 6, 9, 11
    # months with 31 days: 1, 3, 5, 7, 8, 10, 12
    # months with leap year: 2
    # shM is a list of short months in the year (excludes feb since feb is and odd case), 30 days
    # lnM is a list of long months in the year, 31 days
    shM = [4, 6, 9, 11]
    lnM = [1, 3, 5, 7, 8, 10, 12]

    # year check
    if not (2000 <= y):
        # error
        return -1

    # month check
    if 1 <= m <= 12:
        # day check in month check because the number of days in a month is dependent on the month
        if not (m in lnM):
            if not (m in shM):
                # check for leap year
                if (y % 4) == 0:
                    # is a leap year 1 - 29
                    if not (1 <= d <= 29):
                        # error
                        return -1
                else:
                    # is not a leap year 1 - 28
                    if not (1 <= d <= 28):
                        # error
                        return -1
            else:
                # short month
                if not (1 <= d <= 31):
                    # error
                    return -1
        else:
            # long month
            if not (1 <= d <= 30):
                # error
                return -1
    else:
        # error
        return -1

    return fDate
