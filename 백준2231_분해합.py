import sys
read = sys.stdin.readline

n = int(read())


for i in range(1, n):
    arr = list(map(int, str(i)))
    arr.append(i)
    if sum(arr) == n:
        print(i)
        exit()

print(0)


