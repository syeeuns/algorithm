import sys
read = sys.stdin.readline

n = int(read())
k = int(read())
sensor = sorted(list(map(int, read().split())))
sensor_set = set(sensor)
# print(sensor_set)
# '센서 개수 <= 집중국 개수' 면 바로 종료
if len(sensor_set) <= k:
    print(0)
    exit()

diff = []
for i in range(len(sensor) - 1):
    diff.append(sensor[i+1] - sensor[i])

diff = sorted(diff, reverse=True)
print(sum(diff[k-1:]))

# 집중국 k개면 diff에서 k-1 개를 제낄 수 있음

# 1 6 9 3 6 7
# 1 3  6 7 9