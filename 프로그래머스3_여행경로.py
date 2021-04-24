# 45분

from collections import defaultdict


def solution(tickets):
    answer = []
    path = []
    stack = ['ICN']
    flight = defaultdict(list)
    for one in tickets:
        flight[one[0]].append(one[1])
    for k in flight:
        flight[k].sort()

    def dfs():
        while stack:
            if len(flight[stack[-1]]) == 0 or not flight[stack[-1]]:
                path.append(stack.pop())
            else:
                stack.append(flight[stack[-1]].pop(0))

    dfs()
    answer = path[::-1]
    return answer