import math

a, b, n = 0, 0, 50
for l in open("data/input01.txt").readlines():
    d, c = l[0], int(l.strip()[1:])
    prev = n
    a += n == 0
    n += (c if d == "L" else -c)
    b += math.ceil(abs(n / 100) - 0.99)
    b += prev > 0 and n <= 0
    n %= 100
print(a, b)