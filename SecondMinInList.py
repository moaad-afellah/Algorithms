def minElementList_moaad(numbers):
    numbers = list(set(numbers))
    if len(numbers) <=1:
        return None

    for i in range(0, 2):
        min = numbers[0]
        for currentNumber in numbers:
            if min > currentNumber:
                min = currentNumber
        numbers.remove(min)
    return min


assert minElementList_moaad([1, 45, 78, -8, -8]) == 1
assert minElementList_moaad([1, 45, 0, -8, -8]) == 0