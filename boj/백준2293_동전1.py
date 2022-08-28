import sys
read = sys.stdin.readline

n, k = map(int, read().split())
coin = []
for i in range(n):
    coin.append(int(read()))

coin = sorted(coin)
dp = [0 for _ in range(k+1)]
dp[0] = 1

for one in coin:
    for i in range(one, k+1):
        dp[i] += dp[i - one]

print(dp[k])

