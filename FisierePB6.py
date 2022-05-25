n = int(input('Alege n:'))

file = open('FisierePB6.csv', 'w+')
for i in range(1, n):
    for j in range(1, n*n):
        if j % i != 0:
            file.write(str(j))
            file.write('\n')
file.seek(0)
linii = file.readlines()
for linie in linii:
    linie = int(linie[:-1])
print(linie)
