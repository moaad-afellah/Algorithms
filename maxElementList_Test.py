from maxElementList import maxElementList_moaad

n = [1, 2, -45, 10, 25, 120, 458, 78]
p = [1, 2, -45]
vide = []
one = [14]

tab = [-4, -8, -1]

assert maxElementList_moaad(p) == 2
assert maxElementList_moaad(n) == 458
assert maxElementList_moaad(one) == one[0]
assert maxElementList_moaad(vide) is None
assert maxElementList_moaad(tab) == -1
