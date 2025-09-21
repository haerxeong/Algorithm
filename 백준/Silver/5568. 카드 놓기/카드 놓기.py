from itertools import permutations as pm

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
ans = set()

for i in pm(cards, k):
    temp = ''
    for j in i:
        temp += j
    ans.add(int(temp))

print(len(ans))