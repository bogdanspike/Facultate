# Scrieți un program care citește de la tastatură n și afișează primele n numere prime.
# Exemplu: se citește n = 5, se afișează 2, 3, 5, 7, 11.

x = int(input('Numar:'))
l = []

for d in range(100):
    if d == 0 or d == 1:
        pass
    elif d % 2 != 0:
        l.append(d)
    if len(l) == x:
        break

print(l)