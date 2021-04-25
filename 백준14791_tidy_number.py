import sys
read = sys.stdin.readline

# 시간초과 안나게 어떻게 풀지 ?? ? ?  ??
t = int(read())
for k in range(t):
    int_n = int(read())
    for x in range(int_n, 0, -1):
        str_x = str(x)
        arr_x = list(str_x)
        flag = True
        for i in range(len(arr_x)-1):
            if arr_x[i] > arr_x[i+1]:
                print(x, i)
                flag = False
                break
        if flag:
            print(f'Case #{k+1}: {x}')
            break

