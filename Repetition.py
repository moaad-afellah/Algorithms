def isThereElmentDuplicate(listOfNumber):
    num = 0

    while num < len(listOfNumber):
        for repetitionNumber in listOfNumber[num + 1:]:
            if listOfNumber[num] == repetitionNumber:
                return True
        num = num + 1
    return False


def isThereElementDuplicateByDict(listOfNumber):
    dict = {}
    for i in listOfNumber:
        if dict.get(i) is None:
            dict[i] = 1
        else:
            dict[i] = dict[i] + 1
            return True
    return False


assert isThereElmentDuplicate([1, 2, 12, 2]) == True
assert isThereElmentDuplicate([1, 2, 12]) == False
assert isThereElmentDuplicate([445455, 15, 75, 455, 45445, 445455]) == True
assert isThereElmentDuplicate([0, 0]) == True
assert isThereElmentDuplicate([]) == False
assert isThereElmentDuplicate([i for i in range(100)]) == False

assert isThereElementDuplicateByDict([1, 2, 12, 2]) == True
assert isThereElementDuplicateByDict([1, 2, 12]) == False
assert isThereElementDuplicateByDict([445455, 15, 75, 455, 45445, 445455]) == True
assert isThereElementDuplicateByDict([0, 0]) == True
assert isThereElementDuplicateByDict([]) == False
assert isThereElementDuplicateByDict([i for i in range(1000000)]) == False
