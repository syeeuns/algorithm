# 15분
# 최대힙, 최소힙을 동시에 만들어야하나?
# 이걸 꼭 힙으로 만들필요없네 훼이크 ;;
def solution(operations):
    answer = []
    # heap = []
    arr = []
    for one in operations:
        if one[0] == 'I':
            # heapq.heappush(heap, )
            arr.append(int(one[2:]))
        elif one == 'D -1' and arr:
            arr.remove(min(arr))
        elif one == 'D 1' and arr:
            arr.remove(max(arr))
    if len(arr) == 0:
        answer = [0, 0]
    else:
        answer = [max(arr), min(arr)]
    return answer

