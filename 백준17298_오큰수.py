import sys
read = sys.stdin.readline

n = int(read())
arr = list(map(int, read().split()))

stack = []
answer = []
for i in range(n-1, -1, -1):
    while stack:
        if stack[-1] > arr[i]:
            answer.append(stack[-1])
            break
        else:
            stack.pop()

    if not stack:
       answer.append(-1)
    stack.append(arr[i])

print(*answer[::-1])

# 풀이시간 20분