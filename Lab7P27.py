# Alegeți două numere aleatorii folosind a = random.randint(100,1000) și b = random.randint(10,100).
# Apoi generați b liste cu cîte a elemente. Scrieți listele drept linii într-un fișier CSV (folosind csv.writer).

import csv, random

a = random.randint(1, 5)
b = random.randint(1, 3)
liste = []
d = 0

f = open('Lab7P27.csv', 'w+', newline='\n')
writer = csv.writer(f)

while d <= b:
    c = []
    for i in range(a):
        c.append(i)
    liste.append(c)
    d += 1
# print(liste)

for n in liste:
    writer.writerow(str(i) for i in n)
