import sys
read = sys.stdin.readline

# 풀이시간 : 20분
n = int(read())
dp = [999999 for _ in range(n+1)]
route = [999999 for _ in range(n+1)]
dp[1] = 0
route[1] = 0

for i in range(1, n+1):
    if 3*i <= n:
        tmp = dp[3*i]
        dp[3*i] = min(dp[3*i], dp[i] + 1)
        if tmp != dp[3*i]:
            route[3*i] = i
    if 2*i <= n:
        tmp = dp[2 * i]
        dp[2*i] = min(dp[2*i], dp[i] + 1)
        if tmp != dp[2*i]:
            route[2*i] = i
    if i+1 <= n:
        tmp = dp[i + 1]
        dp[i+1] = min(dp[i+1], dp[i] + 1)
        if tmp != dp[i+1]:
            route[i+1] = i

print(dp[n])
while True:
    print(n, end=' ')
    n = route[n]
    if n == 0: break

