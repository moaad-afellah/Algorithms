def isTwoListAreEqual(list1, list2):
    if len(list1) != len(list2):
        return False


    num = 0
    while num < len(list1):
        number1 = list1[num]
        number2 = list2[num]
        if number1 != number2:
            return False
        num = num + 1
    return True


assert isTwoListAreEqual([1, 2, 4, 454], [1, 2, 4, 454]) == True
assert isTwoListAreEqual([454], [1, 2, 4, 454]) == False
assert isTwoListAreEqual([1, 45, 454122, 54], []) == False
assert isTwoListAreEqual([1, 2], [1, 2]) == True
assert isTwoListAreEqual([-1, 0, 3, -48], [-1, 0, 3, -48]) == True
assert isTwoListAreEqual([-48], [-48]) == True
assert isTwoListAreEqual([-48], []) == False
assert isTwoListAreEqual([], []) == True


