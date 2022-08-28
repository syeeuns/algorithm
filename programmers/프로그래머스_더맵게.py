import sys
import heapq
read = sys.stdin.readline


def solution(scoville, k):
    answer = 0
    newS = []
    for one in scoville:
        heapq.heappush(newS, one)
    while newS:
        first = heapq.heappop(newS)
        if first >= k:
            break

        if not newS:
            answer = -1
            break

        second = heapq.heappop(newS)
        new = heapq.heappush(newS, first + 2*second)
        answer += 1

    return answer


# scoville = [1, 2, 3, 9, 10, 12]
scoville = [99,99,99,1]
k = 7
print(solution(scoville, k))


# 최소힙으로 만들어서 힙팝하고 만들고 다시 넣고
# 전체 원소 k 이상될때까지 반복 -> 힙팝한게 k 이상