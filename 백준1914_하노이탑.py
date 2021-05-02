import sys
read = sys.stdin.readline
# 풀이시간 35분

# def hanoi(start, end, n):
#     if n == 0:
#         return 0
#     else:
#         hanoi(start, 6 - (start + end), n - 1) # 하나 적은 원반들 다른 기둥으로 이동
#         print(start, end) # 맨아래 원반을 목적지로
#         hanoi(6 - (start + end), end, n - 1) # 하나 적은 원반들 목적지로 이동

def hanoi(start, end, n):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(start, 6 - (start + end), n - 1) # 하나 적은 원반들 다른 기둥으로 이동
        print(start, end) # 맨아래 원반을 목적지로
        hanoi(6 - (start + end), end, n - 1) # 하나 적은 원반들 목적지로 이동


n = int(read())
if n > 20:
    print(2**n - 1)
else:
    print(2**n - 1)
    hanoi(1, 3, n)
