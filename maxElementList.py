def maxElementList_moaad(listNumber):
    if listNumber == []:
        return None
    max = listNumber[0]
    for numberX in listNumber:
        if max < numberX:
            max = numberX
        elif max >= numberX:
            max = max
    return max
