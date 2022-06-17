from CommonLibrary.Input.ControllerInput import input_Int

def problem3N (number):
    listFois = []
    fois = 0
    while number != 1:
        div = number % 2
        if div == 0:
            number = number / 2
        elif div == 1:
         number = number * 3 + 1
        fois+=1
        listFois.append(number)
    return fois, listFois