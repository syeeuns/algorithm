# 20분
# 내 처음 풀이
# def solution(numbers, target):
#     answer = 0
#     bit_len = 2**len(numbers)
#     num_len = len(numbers)
#     for i in range(bit_len):
#         bit = bin(i)[2:].zfill(num_len)
#         tmp = 0
#         for j in range(num_len):
#             if bit[j] == '0':
#                 tmp -= numbers[j]
#             elif bit[j] == '1':
#                 tmp += numbers[j]
#         if tmp == target:
#             answer += 1
#     return answer

# dfs 풀이
def solution(numbers, target):
    answer = 0
    def dfs(numbers, target, i, tmp):
        result = 0
        if i == len(numbers):
            if tmp == target:
                return 1
            else:
                return 0
        result += dfs(numbers, target, i + 1, tmp + numbers[i])
        result += dfs(numbers, target, i + 1, tmp - numbers[i])
        return result

    answer = dfs(numbers, target, 0, 0)
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))