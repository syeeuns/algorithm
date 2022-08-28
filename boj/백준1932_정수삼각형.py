import sys
read = sys.stdin.readline

n = int(read())
triangle = [list(map(int, read().split())) for _ in range(n)]
dp = [[0 for j in range(i+1)] for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = triangle[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

print(max(dp[n-1]))
