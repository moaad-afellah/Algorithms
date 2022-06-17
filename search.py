from CommonLibrary.Input.ControllerInput import input_Int


def search(list, number):
    for i in list:
        if i == number:
            return True
    return False

assert search([8], 8) == True
assert search([1, 5], 5) == True
assert search([], 1) == False
assert search([8], 8) == True
assert search([8, 1, 45, 1554, 54, 45], 45) == True
