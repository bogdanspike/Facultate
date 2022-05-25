# Scrieți un program care citește de la tastatură n, apoi o listă de n numere întregi diferite și
# afișează media numerelor din listă, apoi cîte numere sînt mai mici decît media și
# cîte sînt mai mari decît media. Exemplu: se citește n = 4, apoi lista [1, 6, -2, 4].
# Se afișează media = 2.25, apoi 2 numere mai mici și 2 numere mai mari.

x = int(input('Numar:'))
l = []
sum = 0
med = 0
mic = 0
mare = 0

for i in range(0, x):
    if len(l) != x:
        l.append(int(input('Numar intreg:')))
    elif len(l) == x:
        break
print(l)

for i in l:
    sum = (sum + i)
    med = sum / len(l)
print(med)

for i in l:
    if i > med:
        mare += 1
    elif i < med:
        mic += 1
print(f'Numere mai mici decat media: {mic}')
print(f'Numere mai mari decat media: {mare}')
