def swape(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2


def selectionSort(listNumber):
    indexList = 0
    while indexList < len(listNumber):
        smallNumber = listNumber[indexList]
        for i in range(indexList + 1, len(listNumber)):
            if listNumber[i] < smallNumber:
                smallNumber = listNumber[i]
                listNumber[indexList], listNumber[i] = swape(listNumber[indexList], listNumber[i])
        indexList = indexList + 1
    return listNumber


assert selectionSort([2, 5, 1]) == [1, 2, 5]
assert selectionSort([2]) == [2]
assert selectionSort([]) == []
assert selectionSort([2, 5, 1, -1, 200, -78, 10]) == [-78, -1, 1, 2, 5, 10, 200]
