
def searchElementInArray(list, number):
    for i in list:
        if i == number:
            return True
    return False


assert searchElementInArray([8], 8) == True
assert searchElementInArray([1, 5], 5) == True
assert searchElementInArray([], 1) == False
assert searchElementInArray([8], 8) == True
assert searchElementInArray([8, 1, 45, 1554, 54, 45], 45) == True
