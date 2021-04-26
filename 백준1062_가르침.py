import sys
read = sys.stdin.readline

n, k = map(int, read().split())

if k < 5:
    print(0)
    exit()

k -= 5
arr = []
a = {'a', 'n', 't', 'c', 'i'}
for i in range(n):
    arr.append(list(set(read().rstrip()) - a))

arr.sort(key=len)
arr = list(filter(lambda x: len(x) <= k, arr))
print(arr)
if k == 0:
    cnt = 0
    for one in arr:
        if len(one) == 0:
            cnt += 1
        else:
            break
    print(cnt)
    exit()

else:
    cnt = 0
    idx = 0
    # 길이 0인거 먼저 셈
    for one in arr:
        if len(one) == 0:
            cnt += 1
        else:
            idx = arr.index(one)
            break

    # 길이 0 아닌 애들
    teach = set()
    for i in range(idx, len(arr)):
        flag = True
        length = len(arr[i])
        for j in range(length):
            teach.add(arr[i][j])
            if len(teach) > k and j != length - 1:
                flag = False
            # elif len(teach) == k:
            #     break
        if flag:
            if len(teach) > k:
                break
            cnt += 1
        else:
            break

    print(cnt)

# 반례
# 6 6
# antarctica
# antahellotica
# antazzztica
# antazzztica
# antazzztica
# antazzztica
# r, z, z, z, z
# r 1개 인식하고 끝나버림
# 더 많은 애를 선택하도록 알고리즘 수정필요