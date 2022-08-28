# 11 12 13
# 21 22 23
# 31 32 33
#
# 1 2 3 2 4 6 3 6 9
# 1 2 2 3 3 4 6 6 9

# 구구단이 n*n 까지가 합쳐진 배열
# 그냥 배열로 하면 무조건 메모리 초과
# 도수정렬로 나오는 개수 세서 해보자 -> 이것도 메모리초과 ;;
# 근데 애초에 입력이 너무 커서 곱 다 구하면 n제곱이라 시간초과 나겠구나

# 솔루션
# 우리는 이분 탐색으로 어떤 수보다 작은 자연수의 곱(i * j)이 몇 개인지 알아낼 것이다.
# A보다 작은 숫자가 몇개인지 찾아내면 A가 몇 번째 숫자인지 알 수 있다.
# 10 * 10에서 20보다 작거나 같은 수를 생각해보자.
# 20을 행으로 나눈 몫

# 풀이시간 40분

import sys
read = sys.stdin.readline

n = int(read())
k = int(read())

start = 1
end = n*n
answer = 0
while start <= end:
    mid = (start + end) // 2
    # mid 보다 작은 숫자들 찾자
    low_rows = mid // n
    cnt = low_rows * n
    for i in range(low_rows + 1, n+1):
        temp = mid // i
        if temp == 0 : break
        cnt += temp
    if cnt < k:
        start = mid + 1
    elif cnt >= k:
        answer = mid
        end = mid - 1

print(answer)