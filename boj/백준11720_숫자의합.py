import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().rstrip()))

print(sum(arr))