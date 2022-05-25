# Scrieți un program care să citească de la tastatură un număr natural n,
# să scrie într-un fișier n numere aleatorii între 1 și 1000 și să afișeze pe ecran maximul lor.

import random

n = int(input('Alege n: '))
max = 0

file = open('Fisiere1.csv', 'w+')
for i in range(n):
    p = str(random.randint(1, 1000))
    file.write(p)
    file.write('\n')

file.seek(0)
linii = file.readlines()
for linie in linii:
    if int(linie) > max:
        max = int(linie)
print(max)
