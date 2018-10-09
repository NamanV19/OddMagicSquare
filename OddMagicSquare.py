number = int(input("Please enter a number"))
x = 0
y = int((number-1)/2)
b = 2

OddMagicNumber = []


for i in range (0, number):
    OddMagicNumber.append([])
    for j in range (0, number):
        OddMagicNumber[i].append(0)

OddMagicNumber[x][y] = 1

while b <= number*number:
    r = x-1
    u = y+1
    if r < 0:
        r = x-1+number
    if u >= number:
        u = y+1-number
    if OddMagicNumber[r][u] != 0:
        r = x+1
        u = y

    x = r
    y = u

    OddMagicNumber[x][y] = b
    b = b+1

for r in OddMagicNumber:
    print(r)














