import sys
read = sys.stdin.readline

n = int(read())
towers = list(map(int, read().split()))
stack = [(1, towers[0])]
result = [0]

for i in range(1, n):
    while stack:
        if stack[-1][1] < towers[i]:
            stack.pop()
        else:
            result.append(stack[-1][0])
            break

    if not stack:
        result.append(0)
    stack.append((i+1, towers[i]))

print(*result)