def solution(answers):
    a = [1, 2, 3, 4, 5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    correct = [[1,0], [2,0], [3,0]]
    for i in range(len(answers)):
        if answers[i] == a[i]:
            correct[0][1] += 1
        if answers[i] == b[i]:
            correct[1][1] += 1
        if answers[i] == c[i]:
            correct[2][1] += 1
    correct.sort(key=lambda x:-x[1])
    if correct[0][1] != correct[1][1]:
        return [correct[0][0]]
    else:
        if correct[1][1] != correct[2][1]:
            return [correct[0][0], correct[1][0]]
        else:
            return [correct[0][0], correct[1][0], correct[2][0]]


answers = [1,2,3,4,5]
print(solution(answers))

# 문제 이해 잘못  20분 ㅠ
