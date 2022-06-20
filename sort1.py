def swape(number1, number2):
    temp = number1
    number1 = number2
    number2 = temp
    return number1, number2


def sort1(listnumber):
    num = 0
    while num < len(listnumber):
        smallnumber = listnumber[num]
        for i in range(num + 1, len(listnumber)):
            if listnumber[i] < smallnumber:
                smallnumber = listnumber[i]
                listnumber[num], listnumber[i] = swape(listnumber[num], listnumber[i])
        num = num + 1
    return listnumber


assert sort1([2, 5, 1]) == [1, 2, 5]
assert sort1([2]) == [2]
assert sort1([2, 5, 1, -1, 200, -78, 10]) == [-78, -1, 1, 2, 5, 10, 200]
