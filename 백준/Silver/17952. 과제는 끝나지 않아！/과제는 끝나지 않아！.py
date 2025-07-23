input = __import__('sys').stdin.readline

stack = []
score = 0
for _ in range(int(input())):
    task = list(map(int, input().split()))
    
    if not task[0]:
        if stack: task = stack.pop()
        else: continue
    
    task[-1] -= 1
    if not task[-1]:
        score += task[1]
    else:
        stack.append(task)

print(score)