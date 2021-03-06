import numpy as np

from collections import defaultdict
from scipy.ndimage import convolve

store = set()
min_x = min_y = min_z = max_z = 0
with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line.strip()):
            if c == '#':
                store.add((x,y,0))
max_x, max_y = x, y

def neighbours(store, x, y, z):
    positive = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                if i == j == k == 0:
                    continue
                else:
                    if (x+i, y+j, z+k) in store:
                        positive+=1
    return positive

for iteration in range(1, 7):
    tmp_store = set()
    for x in range(min_x - iteration, max_x + iteration+1):
        for y in range(min_y - iteration, max_y + iteration+1):
            for z in range(min_z - iteration, max_z + iteration+1):
                n = neighbours(store, x, y, z)
                if (x, y, z) in store and n in [2, 3]:
                    tmp_store.add((x, y, z))
                if (x, y, z) not in store and n == 3:
                    tmp_store.add((x, y, z))
    store = tmp_store
print(len(store))
