import sys
read = sys.stdin.readline

k, n = map(int, read().split())
lan = []
for i in range(k):
    lan.append(int(read()))

print(lan)