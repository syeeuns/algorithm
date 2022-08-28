import sys
read = sys.stdin.readline

def solution(prices):
    n = len(prices)
    answer = [0 for i in range(n)]
    answer[n-1] = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if prices[j] >= prices[i]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))