brackets = input()
stack = []
length = 0
ans = 0
flag = False

for bracket in brackets:
    if bracket == '(':
        stack.append(bracket)
        length += 1
        flag = True
    else:
        if stack[-1] == '(' and flag:  # 레이저
            stack.pop()
            length -= 1
            ans += length
        else:   # 오른쪽 괄호
            stack.pop()
            length -= 1
            ans += 1
        flag = False

print(ans)
