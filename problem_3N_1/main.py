from problem3N_1 import problem3N

number = input("Number: ")

i = 1
while i <= int(number):
    fois, listFois = problem3N(i)
    # print(i , "     ", listFois)
    i += 1
