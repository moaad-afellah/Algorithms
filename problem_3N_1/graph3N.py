from problem3N_1 import problem3N

i = 1
lineFois = []
while i <= int(100):
    fois, listFois = problem3N(i)
    lineFois = lineFois + [fois]
    i += 1

print(list(range(1, 101)))
print(lineFois)
