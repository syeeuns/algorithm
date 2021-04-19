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

    # 길이 0인거 먼저 셈
    for one in arr:
        if len(one) == 0:
            cnt += 1
        else:
            break
    while k != 0:
        for one in arr:
            if len(one) == 0:
                continue





# a, n, t, i, c   최소 5개는 배워야 글 읽을 수 있음

# 5개 이상인 경우
# 주어진 문자열의 문자 종류로 list 만든다
# 위 문자 제거하고, list 만든다
# 남은 k 만큼, 배울수있는 단어가 최대가 되도록 함
# 길이순 오름차순 정렬
# 젤 작은거 선택하고 돌면서 그거 다 지움
#