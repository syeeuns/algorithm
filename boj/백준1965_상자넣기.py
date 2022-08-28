import sys
read = sys.stdin.readline

n = int(read())
boxes = list(map(int, read().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



# 풀이시간 12분

# 1 2(1,6) 2(1,2) 3(1,2,5) 4(1,2,5,7) 3(1,2,3) 4(1,2,3,5) 5(1,2,3,5,6)
# 자기보다 이전 상자이면서 자기보다 작은 상