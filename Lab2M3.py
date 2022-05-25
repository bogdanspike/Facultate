x = int(input('Numar:'))
l = []
m = []

for i in range (0, x):
    if len(l) != x:
        print('Alege cuvant:')
        l.append(input(''))
    print(l)
    if len(l) == x:
        break
for i in l:
    m.append(i[0])
print(m)