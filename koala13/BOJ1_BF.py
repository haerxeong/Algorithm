#13423 Three dots (멍청한ver)
'''from itertools import combinations as cb
t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    dots = list(map(int, input().split()))
    for x, y, z in cb(sorted(dots), 3):
        if y - x == z - y:
            ans += 1
    print(ans)'''

'''from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    dots = sorted(list(map(int, input().split())))
    spotSet = set(dots)
    
    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            third = dots[j] + (dots[j] - dots[i])
            if third in spotSet:
                ans += 1
    print(ans)'''

#15654: N과 M (5)
'''from itertools import permutations as pm

n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in pm(sorted(num), m):
        print(' '.join(map(str, i)))'''

#3040: 백설 공주와 일곱 난쟁이
'''from itertools import combinations as cb
n = []
for _ in range(9):
    n.append(int(input()))
for i in cb(n, 7):
    if sum(i) == 100:
        print('\n'.join(map(str, i)))
        break
'''

#1969: DNA
'''n, m = map(int, input().split())
input_dna = [input() for _ in range(n)]
ans = ""
dna = ['A', 'C', 'G', 'T']

for i in range(m): 
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        dic[input_dna[j][i]] += 1
    max_frequency = max(dic.values())
    most_common_bases = [base for base, frequency in dic.items() if frequency == max_frequency]
    ans += most_common_bases[0]

print(ans)

dis = 0
for s in input_dna:
    for i in range(m):
        if ans[i] != s[i][0]:
            dis += 1

print(dis)'''

#15663: N과 M (9)
from itertools import permutations as pm

n, m = map(int, input().split())
num = map(int, input().split())

for i in sorted(set(pm(num, m))):
    print(' '.join(map(str, i)))
print(num)