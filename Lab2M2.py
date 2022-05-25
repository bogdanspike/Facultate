x = int(input('Numar:'))

for d in range(x, 2 * x):
    if d % 2 != 0 and d > x:
        print(d)
        break