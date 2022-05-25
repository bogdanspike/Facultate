# Se dă un număr n de la tastatură. Să se afișeze suma divizorilor săi, precum și lista divizorilor acestei sume.
# Exemplu: n = 20, se afișează Suma divizorilor: 1 + 2 + 4 + 5 + 10 + 20 = 42 și [1, 2, 3, 6, 7, 14, 21, 42].1

n = int(input('Introduceti un numar n:'))
suma_divizori = 0
lista_divizori = []

for i in range(1, n):
    if n % i == 0:
        suma_divizori = suma_divizori + i
        lista_divizori.append(i)

print(suma_divizori)
print(lista_divizori)