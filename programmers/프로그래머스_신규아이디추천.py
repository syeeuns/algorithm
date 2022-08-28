def solution(new_id):
    answer = list(new_id.lower())
    new = []
    # step2
    for one in answer:
        if one.isalnum() or one in "-_.":
            new.append(one)
    # step3
    answer = new
    new = [answer[0]]
    for i in range(1, len(answer)):
        if answer[i] == '.' and answer[i-1] == '.':
            continue
        else: new.append(answer[i])
    #step4
    if len(new) > 0 and new[0] == '.':
        new = new[1:]
    if len(new) > 0 and new[-1] == '.':
        new = new[:-1]
    #step5
    if len(new) == 0:
        new.append("a")
    #step6
    if len(new) > 15:
        new = new[:15]
    if new[-1] == '.':
        new = new[:-1]
    #step7
    if len(new) < 3:
        n = 3 - len(new)
        for i in range(n):
            new.append(new[-1])
    answer = new
    new = []
    return ''.join(answer)


new_id = "...!@BaT#*..y.abcdefghi...jklm....."
new_id= "...."

print(solution(new_id))


# 30분 (isalnum!!!!)