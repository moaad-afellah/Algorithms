def isThereDuplicate(listOfNumber):
    num = 0

    while num < len(listOfNumber):
        for repetitionNumber in listOfNumber[num + 1:]:
            if listOfNumber[num] == repetitionNumber:
                return True
        num = num + 1
    return False


def isThereDuplicateByDict(listOfNumber):
    dict = {}
    for i in listOfNumber:
        if dict.get(i) is None:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
            return True
    return False


assert isThereDuplicate([1, 2, 12, 2]) == True
assert isThereDuplicate([1, 2, 12]) == False
assert isThereDuplicate([445455, 15, 75, 455, 45445, 445455]) == True
assert isThereDuplicate([0, 0]) == True
assert isThereDuplicate([]) == False
assert isThereDuplicate([i for i in range(100)]) == False

assert isThereDuplicateByDict([1, 2, 12, 2]) == True
assert isThereDuplicateByDict([1, 2, 12]) == False
assert isThereDuplicateByDict([445455, 15, 75, 455, 45445, 445455]) == True
assert isThereDuplicateByDict([0, 0]) == True
assert isThereDuplicateByDict([]) == False
assert isThereDuplicateByDict([i for i in range(10000000)]) == False
