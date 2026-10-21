def solution(s):
    answer = True
    stack = []

    for ss in s:
        if ss == '(':
            stack.append(ss)
        else:
            if stack: stack.pop()
            else: return False

    if stack: answer = False

    return answer