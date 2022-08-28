# 풀이시간 : 25분
def solution(intervals):
    # 시작 시간 or 종료 시간 기준 정렬
    # 시작 시간 기준 정렬한다면, 사라져야 하는 케이스
    # 1. 시작 시간 같고, 종료 시간 작거나 같음
    # 2. 시작 시간 더 크고, 종료 시간 작거나 같음
    # -> 시작 시간이 크거나 같고, 종료 시간이 작거나 같음
    length = len(intervals)
    answer = set()
    intervals.sort(key=lambda x:(x[0], -x[1]))
    print(intervals)
    i = 0
    j = 0
    while j < length:
        if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
            answer.add(intervals[i])
            j += 1
        else:
            i = j
    return sorted(list(answer), key=lambda x:(x[0], -x[1]))


intervals = [(1, 3), (5, 8), (4, 10), (20, 25), (16, 17), (6, 7), (5, 7), (5, 6)]
print(solution(intervals))

# 문제
# 중첩될 수 있는 인터벌들을 갖는 리스트가 있습니다. 중첩되는 인터벌들을 하나로 합친 새로운 리스트를 반환하세요.
# 입력 리스트는 정렬되어 있지 않습니다.
# 예를 들어, [(1, 3), (5, 8), (4, 10), (20, 25)] 가 주어지면, [(1, 3), (4, 10), (20, 25)] 를 반환해야 합니다.