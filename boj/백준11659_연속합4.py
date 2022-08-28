import sys
read = sys.stdin.readline

n, m = map(int, read().split())
arr = list(map(int, read().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]
for k in range(1, len(arr)):
    dp[k] = dp[k-1] + arr[k]

for t in range(m):
    i, j = map(int, read().split())
    if i >= 2:
        answer = dp[j-1] - dp[i-2]
    else:
        answer = dp[j-1]
    print(answer)