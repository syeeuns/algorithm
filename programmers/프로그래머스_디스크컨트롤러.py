# 시간의 흐름을 기준으로 작업마다 소요된 시간들을 더하는 방법을 생각해보았다.
#
# 첫번째 작업이 시작하는 시간과 첫번째 작업이 끝나는 시간 사이에 들어온 요청들을 우선순위큐에 넣는다.
# 작업이 실행되는 시간동안 들어온 요청들에 대해 현재 작업이 끝나는 시간까지 걸린 시간을 답에 더한다.
#
# 우선순위큐를 pop()하여 작업에 소요되는 시간이 가장 작은 작업을 얻는다.
# 우선순위큐에 들어온 작업들 개수만큼 위에서 얻은 작업의 시간을 답에 더한다.
#
# 현재 작업이 끝나는 시간과 방금 얻은 작업이 끝나는 시간 사이에 들어온 요청들을 우선순위큐에 넣는다.
# 작업이 실행되는 시간동안 들어온 요청들에 대해 현재 작업이 끝나는 시간까지 걸린 시간을 답에 더한다.
#
# 반복...

import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    heap = []
    start = -1 # 이전 작업 시작 시간
    now, i = 0, 0
    while i < n:
        # 사이에 들어온 요청을 힙에 담음
        for one in jobs:
            if start < one[0] <= now:
                heapq.heappush(heap, [one[1], one[0]])
        if heap:
            x = heapq.heappop(heap)
            start = now
            now += x[0]
            answer += now - x[1]
            i += 1
        else:
            now += 1
    return answer // n


jobs = sorted([[0, 3],[1, 9], [2, 6]])
print(solution(jobs))

# 진짜 역대급 모르겠음 . . .