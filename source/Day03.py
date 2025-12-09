a, b = 0, 0
for l in open("data/input03.txt").readlines():
    l, ms = [*map(int, l.strip())], ""
    a_ind = l.index(max(l[:-1]))
    a += l[a_ind]*10 + max(l[a_ind+1:])
    for i in range(-11, 1):
        m = max(l[:len(l)+i])
        ms += str(m)
        l = l[l.index(m)+1:]
    b += int(ms)
print(a, b)