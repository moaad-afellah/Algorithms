def swape(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2


def bubbleSort (listNumber):
    isSwappedHappen = True
    while isSwappedHappen:
        isSwappedHappen = False
        currentElement = 0
        while currentElement < len(listNumber) - 1 :
            if listNumber[currentElement] > listNumber[currentElement + 1]:
                listNumber[currentElement], listNumber[currentElement + 1] = swape(listNumber[currentElement], listNumber[currentElement + 1])
                isSwappedHappen = True
            currentElement = currentElement + 1
    return listNumber



assert bubbleSort([2, 5, 1]) == [1, 2, 5]
assert bubbleSort([2]) == [2]
assert bubbleSort([2, 5, 1, -1, 200, -78, 10]) == [-78, -1, 1, 2, 5, 10, 200]
assert bubbleSort([]) == []
