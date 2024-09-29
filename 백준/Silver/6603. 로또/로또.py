from itertools import combinations as cb

while True:
    S = list(map(int, input().split()))
    if S[0] == 0: break
    for C in cb(S[1::], 6):
        print(' '.join(map(str, C)))
    print()