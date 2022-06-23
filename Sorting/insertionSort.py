def swape(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2


def sort3(listNumber):
    num = 1
    while num < len(listNumber) :
        number = num - 1
        current = num
        while number >= 0:
            if listNumber[number] > listNumber[current]:
                listNumber[number], listNumber[current] = swape(listNumber[number], listNumber[current])
                current = current - 1

            number = number - 1

        num = num + 1
    return  listNumber


assert sort3([2, 5, 1]) == [1, 2, 5]
assert sort3([2]) == [2]
assert sort3([2, 5, 1, -1, 200, -78, 10]) == [-78, -1, 1, 2, 5, 10, 200]
assert sort3([]) == []
