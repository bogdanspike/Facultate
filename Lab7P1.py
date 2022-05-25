# 1.1. Scrieți un program care să primească de la tastatură unul dintre prenumele dumneavoastră
# și să afișeze două șiruri de caractere, unul alcătuit doar din vocalele din prenume,
# iar celălalt alcătuit doar din consoanele din prenume.
# Exemplu: Pentru "Adrian", se afișează "aia" și "drn".

prenume = input('Prenume:')

vocale = ['a', 'e', 'i', 'o', 'u']
consoane = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

vocale_gasite = []
consoane_gasite = []

for i in prenume:
    if i in vocale:
        vocale_gasite.append(i)
    elif i in consoane:
        consoane_gasite.append(i)
print(vocale_gasite)
print(consoane_gasite)