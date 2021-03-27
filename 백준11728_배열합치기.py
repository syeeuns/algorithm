import sys
read = sys.stdin.readline

n, m = map(int, read().split())
a = list(map(int, read().split()))
b = list(map(int, read().split()))

result = sorted(a+b)
for one in result: print(one, end=' ')

