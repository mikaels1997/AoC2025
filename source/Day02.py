a, b = 0, 0
for l in open("data/input02.txt").read().split(","):
    x, y = l.split("-")
    while int(x) <= int(y):
        invs = set()
        for i in range(1, len(x)//2 + 1):
            ext = x[:i] * (len(x) // len(x[:i]))
            if x != ext: continue
            b += (ext not in invs) * int(ext)
            a += (x[:i] * 2 == x) * int(ext)
            invs.add(ext)
        x = str(int(x) + 1)
print(a, b)