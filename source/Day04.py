import numpy as np
from scipy.signal import convolve2d

G = np.array([[x == "@" for x in r.strip()]
     for r in open("data/input03.txt").readlines()], dtype=int)
mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
a, b, r = 0, 0, np.array([1])

while r.sum() > 0:
    ns = convolve2d(G, mask, mode='same') * G + G
    r = ((0 < ns) & (ns < 5))
    if not a: a = r.sum()
    b += r.sum()
    G -= r
print(a, b)