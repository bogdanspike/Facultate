import random
squared_numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = []
for i in range(10):
    if len(a) < 10:
        a.append(random.randint(1, 100))
    if a[i] in squared_numbers:
        print("Numarul este:", a[i])
    #    print("Pozitia lui este:", i)
print(a)
