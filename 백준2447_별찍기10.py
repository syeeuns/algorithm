import sys
read = sys.stdin.readline


def divide(x, y, leng):
    if leng == 1:
        board[x][y] = '*'
        return
    div = int(leng / 3)
    divide(x, y, div)
    divide(x, y+div, div)
    divide(x, y+(2*div), div)
    divide(x+div, y, div)
    divide(x+div, y+(2*div), div)
    divide(x+(2*div), y, div)
    divide(x + (2 * div), y+div, div)
    divide(x + (2 * div), y+(2*div), div)


n = int(read())
board = [[' ' for _ in range(n)] for _ in range(n)]
divide(0, 0, n)

for i in range(n):
    for j in range(n):
        print(board[i][j], end='')
    print()

# 분할정복 : 나눌 단위, 기저케이스 정함 -> 기저케이스까지 재귀 돌린다
# 영역을 9분할해서 5번째 영역만 비우고
# 나머지 영역에는 현재의 1/3 짜리 사각형 찍는다


