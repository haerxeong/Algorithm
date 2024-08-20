'''t = int(input())

gandalf_scores = [1, 2, 3, 3, 4, 10]
sauron_scores = [1, 2, 2, 2, 3, 5, 10]

for i in range(1, t+1):
    gandalf = list(map(int, input().split()))
    sauron = list(map(int, input().split()))
    
    gandalf_score = 0
    sauron_score = 0
    
    for j in range(6):
        gandalf_score += gandalf_scores[j] * gandalf[j]
        
    for k in range(7):
        sauron_score += sauron_scores[k] * sauron[k]
        
    if gandalf_score > sauron_score:
        print("Battle %d: Good triumphs over Evil"%i)
        
    elif sauron_score > gandalf_score:
        print("Battle %d: Evil eradicates all trace of Good"%i)
        
    else:
        print("Battle %d: No victor on this battle field"%i)'''

'''a, b, v = map(int, input().split())
day = (v - b - 1) // (a - b) + 1
print(day)'''

n = int(input())
pat = input()
for i in range(n):
    file_name = input()
    if file_name[0] == pat[0] and file_name[-1] == pat[-1]:
        print("DA")
    else:
        print("NE")