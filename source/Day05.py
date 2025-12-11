rs, irs = open("data/input05.txt").read().split("\n\n")
a, b, mx = set(), 0, 0

for r in sorted(rs.split("\n"), key=lambda x: int(x.split('-')[0])):
    prs = [*map(int, r.strip().split("-"))]
    if prs[0] > mx:
        b += prs[1] - prs[0] +1
    elif prs[0] <= mx and prs[1] > mx:
        b += prs[1] - mx
    if prs[1] > mx: mx = prs[1]
    for ir in irs.split("\n"):
        if prs[0] <= int(ir) <= prs[1]:
            a.add(int(ir))

print(len(a), b)