import sys
from itertools import combinations
read = sys.stdin.readline

n, m = map(int, read().split())
arr = list(map(int, read().split()))

candidate = list(combinations(arr, 3))
ans = 0
for one in candidate:
    a = sum(one)
    if m >= a and ans < a:
        ans = a

print(ans)