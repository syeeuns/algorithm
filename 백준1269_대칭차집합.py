import sys
read = sys.stdin.readline

n, m = map(int, read().split())
a = set(map(int, read().split()))
b = set(map(int, read().split()))

print(len(a-b) + len(b-a))