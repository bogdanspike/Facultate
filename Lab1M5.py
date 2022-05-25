# Scrieți un program care citește de la tastatură un număr n de maximum 10 cifre și
# afișează dacă acesta este palindrom (adică dacă este egal cu răsturnatul său).
# Exemplu: se citește n = 44155144 și se afișează DA

x = int(input("Numar:"))
initial = x
invers = 0

while x > 0:
    cifra = x % 10
    invers = invers * 10 + cifra
    x = x // 10
if initial == invers:
    print("DA")
else:
    print("NU")

