# Se dau două numere de la tastatură. Să se afișeze divizorii lor comuni.
# Exemplu: n = 20, m = 12, se afișează 1, 2, 4.

import random

n = int(input('Introdu anul nasterii:'))
numere = []
suma = 0
media = 0
numere_peste_medie = []

for i in range(1, n + 1):
    x = random.randint(6, 11)
    numere.append(x)

for i in numere:
    suma = suma + i
    media = suma / n
print(media)

for i in numere:
    if i > media:
        numere_peste_medie.append(i)
print(numere_peste_medie)
