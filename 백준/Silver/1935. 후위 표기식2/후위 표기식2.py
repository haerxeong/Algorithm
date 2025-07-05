N = int(input())
eq = input()
operands = [int(input()) for _ in range(N)]
stack = []

for i in eq:
    if 'A' <= i <= 'Z':
        stack.append(operands[ord(i) - 65])

    else:
        op2 = stack.pop()
        op1 = stack.pop()

        if i == '+':
            stack.append(op1 + op2)
        elif i == '-':
            stack.append(op1 - op2)
        elif i == '*':
            stack.append(op1 * op2)
        else: stack.append(op1 / op2)

print(f"{stack[0]:.2f}")