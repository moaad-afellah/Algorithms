from CommonLibrary.Input.ControllerInput import input_Int
def sourh (number):
    list = [1, 5, 8, 4, 5, 5, 7, 6, 4, 4, 7, 5, 9, 4, 9, 2, 4, 8]

    soursh = 0
    for i in list:
        if i == number:
            soursh = soursh + 1
    print(soursh)
number = input_Int("give me numner: ")
soursh = sourh(number)
print(soursh)
