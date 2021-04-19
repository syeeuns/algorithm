import sys
from itertools import permutations
read = sys.stdin.readline

n = int(read())
arr = [i for i in range(1, n+1)]

result = permutations(arr, n)
for one in result:
    for i in one:
        print(i, end=' ')
    print()