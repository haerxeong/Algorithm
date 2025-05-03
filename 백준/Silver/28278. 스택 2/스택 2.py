input = __import__('sys').stdin.readline

stack = []

for _ in range(int(input())):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack: print(stack.pop())
        else: print(-1)
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)