#9012: 괄호
'''t = int(input())
for _ in range(t):
    brackets = list(input())
    stack = []
    for s in brackets:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                print("NO")
                break
            stack.pop()  
    else: print("NO" if stack else "YES")'''

#12789: 도키도키 간식드리미
n = int(input())
cnt = 1
lines = list(map(int, input().split()))
li = []
for i in lines:
    if i != cnt:
        li.append(i)
    else:
        lines.pop(i)
        cnt += 1
    
    while li:
        if li[-1] == cnt: 
            li.pop()
            cnt += 1
        else: break
print("Sad" if li else "Nice")
        
