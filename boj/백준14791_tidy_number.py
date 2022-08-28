import sys
read = sys.stdin.readline

# 시간초과
# t = int(read())
# for k in range(t):
#     int_n = int(read())
#     for x in range(int_n, 0, -1):
#         str_x = str(x)
#         arr_x = list(str_x)
#         flag = True
#         for i in range(len(arr_x)-1):
#             if arr_x[i] > arr_x[i+1]:
#                 print(x, i)
#                 flag = False
#                 break
#         if flag:
#             print(f'Case #{k+1}: {x}')
#             break


t = int(read())
for k in range(t):
    n = read().rstrip()
    int_n = int(n)
    arr_n = list(map(int, n))
    candidate = []

    if int_n < 10:
        print(f'Case #{k+1}: {int_n}')
        continue

    Flag = True
    for m in range(len(arr_n) - 1):
        if arr_n[m] > arr_n[m + 1]:
            Flag = False
            break
    if Flag:
        print(f'Case #{k + 1}: {int_n}')
        continue


    for i in range(len(arr_n) - 2, -1, -1):
        arr_n[i+1] = 9
        if arr_n[i] != 0:
            arr_n[i] -= 1
        if arr_n[i] == 0 and i != 0:
            arr_n[i] = 9
            arr_n[i-1] -= 1
        flag = True
        for j in range(len(arr_n) - 1):
            if arr_n[j] > arr_n[j+1]:
                flag = False
                break
        if flag:
            answer = ''.join(list(map(str, arr_n)))
            if answer[0] == '0':
                print(f'Case #{k + 1}: {answer[1:]}')
            else:
                print(f'Case #{k + 1}: {answer}')
            break



# 바킹독 풀이

# 조금만 생각해보면 주어진 수에 대해 그 수 이하의 Tidy Number의 형태는 굉장히 뻔하다는 것을 알 수 있습니다.
# 예를 들어 23412362라는 수에 대해, 그 수 이하의 Tidy Number는
#
# 23412359
# 23412299
# 23411999
# 23409999
# 23399999
# 22999999
# 19999999
#
# 중 하나입니다. 특정 자리수를 잡아 그 자리수의 값을 1 감소시키고 하위 자리수는 전부 9로 만드는 것입니다.
# 각 자리에 대해 이것들을 반복 적용하면 됩니다.