import sys
read = sys.stdin.readline

# 풀이시간 10분
# 1. set 풀이   (68ms)
# t = int(read())
#
# for i in range(1, t+1):
#     n = int(read())
#     if n == 0:
#         print(f'Case #{i}: INSOMNIA')
#         continue
#     check = set()
#     k = 1
#     while len(check) != 10:
#         temp = k * n
#         listN = list(str(temp))
#         for one in listN:
#             check.add(one)
#         k += 1
#
#     print(f'Case #{i}: {temp}')



# 2. list, not in     (68ms) 같넹
t = int(read())
allNum = [str(x) for x in range(10)]

for i in range(1, t+1):
    n = int(read())
    if n == 0:
        print(f'Case #{i}: INSOMNIA')
        continue
    check = []
    k = 1
    while len(check) != 10:
        temp = k * n
        listN = list(str(temp))
        for one in listN:
            if one not in check:
                check.append(one)
        k += 1

    print(f'Case #{i}: {temp}')
