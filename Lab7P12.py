# 1.7. Scrieți un program care să citească de la tastatură n, care reprezintă anul nașterii dumneavoastră
# și să genereze aleatoriu o listă de n numere naturale, cu valori între luna nașterii și ziua de naștere.
# Afișați media numerelor generate și ce procent din numărul de numere generate este mai mare decît media.

a = int(input('Primul nr:'))
b = int(input('Al doilea nr:'))

divizori_a = []
divizori_b = []
divizori_comuni = []

for i in range(1, a + 1):
    if a % i == 0:
        divizori_a.append(i)

for j in range(1, b + 1):
    if b % j == 0:
        divizori_b.append(j)

for i in divizori_a:
    for j in divizori_b:
        if i == j:
            divizori_comuni.append(i)

print(divizori_comuni)
