input = __import__('sys').stdin.readline
S = set()
for _ in range(int(input())):
    op = list(input().split())

    if op[0] == 'add': S.add(op[1])
    elif op[0] == 'remove' and op[1] in S: S.remove(op[1])
    elif op[0] == 'check': print(1 if op[1] in S else 0)
    elif op[0] == 'toggle': 
        if op[1] in S: S.remove(op[1])
        else: S.add(op[1])
    elif op[0] == 'all': S = set([str(i) for i in range(1, 21)])
    else: S = set()