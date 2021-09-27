for x in range(1,151):
    print(x)

for y in range(5, 1001, 5):
    print(y)

for z in range(1, 101):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)

added = 0
for a in range(1, 500001):
    if a % 2 != 0:
        added += a
print(added)

for b in range(2018, 0, -4):
    print(b)

lowNum = 4
highNum = 27
mult = 2
for c in range(int(lowNum), int(highNum), int(mult)):
    print(c)