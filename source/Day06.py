data = open("data/input06.txt").readlines()
ops = [*map(str.strip, data[-1].split())]
cols = ["".join(row[x] for row in data[:-1])
        for x in range(len(data[0]) - 1)][::-1]
calc = lambda r, n, o: (r + int(r == 0)) * n if o == "*" else r + n
a, b = 0, 0

for i in range(len(ops)):
    ra, rb = 0, 0
    for ns in data[:-1]:
        n = int(ns.strip().split()[i])
        ra = calc(ra, n, ops[i])
    while len(cols):
        n = cols.pop().strip()
        if not n: break
        rb = calc(rb, int(n), ops[i])
    a, b = a + ra, b + rb
print(a, b)