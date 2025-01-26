n, k, b = map(int,input().split())
min_fix = float('inf')

road = [True]*(n+1)

for _ in range(b):
    road[int(input())] = False

s = 1
e = 1 
fix = 0

while e < k:
    e += 1
    if road[e] == False:
        fix += 1

while e < n: 
    min_fix = min(min_fix, fix)
    e += 1 
    s += 1
    if road[e] == False: 
        fix += 1
    if road[s] == False: 
        fix -= 1

print(min_fix)