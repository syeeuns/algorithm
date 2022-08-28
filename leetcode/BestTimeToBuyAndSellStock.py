# 풀이시간 : 20분
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    length = len(prices)
    buy = 0
    sell = 1
    answer = 0
    while sell < length:
        diff = prices[sell] - prices[buy]
        if diff > 0:
            answer = max(answer, diff)
        else:
            buy = sell
        sell += 1
    return answer


prices = [7,1,5,3,6,4]
print(maxProfit(prices))

# 이것도 n^2 ?!
# 비교하다가 prices[i]보다 prices[j]가 더 작다면 바로 그걸 기준점으로 점프해야함 ;