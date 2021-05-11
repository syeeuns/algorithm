import sys
import heapq
read = sys.stdin.readline

# li = [1,5,2,7,4,2,6,9,10]
li = [1]

print(heapq.heappop(li))
print(li)
print(heapq.heappop(li))