import sys
from collections import deque
read = sys.stdin.readline

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    while on_bridge:
        answer += 1
        on_bridge.popleft()
        if trucks:
            if sum(on_bridge) + trucks[0] > weight:
                on_bridge.append(0)
            else:
                on_bridge.append(trucks.popleft())
    return answer

print(solution(2, 10, [7,4,5,6]))