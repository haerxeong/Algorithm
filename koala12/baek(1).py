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

'''n = int(input())
pat = input()
for i in range(n):
    file_name = input()
    if file_name[0] == pat[0] and file_name[-1] == pat[-1]:
        print("DA")
    else:
        print("NE")'''

'''str_len = int(input())
s = input()

cnt_e = 0
cnt_2 = 0

for i in range(str_len):
    if s[i] == 'e':
        cnt_e += 1
    else:
        cnt_2 += 1
        
if cnt_e > cnt_2:
    print("e")
elif cnt_2 > cnt_e:
    print(2)
else:
    print("yee")'''

'''string = input()
for i in range(len(string) // 10):
        print(string[i * 10 : i * 10 + 10])

if len(string) % 10 != 0:
        print(string[-(len(string) % 10):])'''

'''while True:
    text = input()
    if text == 'END':
        break
    else:
        print(text[-1::])'''

'''alphabets = 'abcdefghijklmnopqrstuvwxyz'
cnt = [0]*26
s = input()
for char in s:
    for i in range(26):
        if char == alphabets[i]:
            cnt[i] += 1
            break
for char in cnt:
    print(char, end = ' ')'''

'''n = int(input())
time_list = list(map(int, input().split()))

fee_y = 0
fee_m = 0

for i in range(n):
    fee_y += (time_list[i] // 30 + 1) * 10

for i in range(n):
    fee_m += (time_list[i] // 60 + 1) * 15
     
if fee_y > fee_m:
    print("M", fee_m)
elif fee_y < fee_m:
    print("Y", fee_y)
else:
    print("Y M", fee_y)'''

'''n, w, h, l = map(int, input().split())
w //= l
h //= l

max_n = w * h

if n < max_n:
    max_n = n

print(max_n)'''

'''num_a = list(map(int, input().split()))
num_b = list(map(int, input().split()))

score_a , score_b = 0, 0

for i in range(10):
    if num_a[i] > num_b[i]:
        score_a += 3
    elif num_a[i] < num_b[i]:
        score_b += 3
    else:
        score_a += 1; score_b += 1

print(score_a, score_b)
    
if score_a > score_b:
    print("A")
elif score_a < score_b:
    print("B")
else:
    if num_a == num_b:
            print("D")
    else:
        for i in range(9, -1, -1):
            if num_a[i] > num_b[i]:
                print("A")
                break
            elif num_a[i] < num_b[i]:
                print("B")
                break'''

'''s, k, h = map(int, input().split())
dic = {s : 'Soongsil', k : 'Korea', h : 'Hanyang'}
if s + k + h >= 100:
    print("OK")
else:
    sorted_keys = sorted(dic.keys())
    min_value = sorted_keys[0]
    print(dic[min_value])'''

'''n, m = map(int, input().split())

s = []
for i in range(n):
    s.append(input())
    
cnt = 0

for i in range(m):
    input_string = input()
    if input_string in s:
        cnt += 1'''

'''n, m = map(int, input().split())

set_n, set_m = set(), set()

for i in range(n):
    set_n.add(input())

for i in range(m):
    set_m.add(input())

common_list = sorted(list(set_n & set_m))   
#교집합을 만드는 과정을 거치기 위헤 리스트가 아닌 set로 설정

print(len(common_list))
for name in common_list:
    print(name)'''

'''num_set = set()
for i in range(10):
    d = int(input())
    num_set.add(d % 42)
    
print(len(num_set))'''

'''n = int(input())
num_list = list(input().split())
for i in sorted(set(num_list)):
    print(i, end = ' ')'''

'''dice_dict = {1:'Yakk', 2:'Doh', 3:'Seh', 4:'Ghar', 5:'Bang', 6:'Sheesh'} 
dice_list = ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    print("Case %d:" % (i + 1), end = ' ')
    
    if a < b:
        a, b = b, a
    if a == b:
        print( dice_list[a - 1])
    elif a == 6 and b == 5:
        print("Sheesh Beesh")
    else:
        print(dice_dict[a], dice_dict[b])'''

'''while True:
    input_string = input()
    
    if input_string == '*':
        break
        
    else:
        alphabet_set = set(input_string)
        
        if len(alphabet_set) >= 26:
            print("Y")
        else:
            print("N")'''

n = int(input())
clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
largest_num, cnt = 0, 0

for i in range(9):
    num_list = list(map(int, input().split()))
    max_value = max(num_list)
    if largest_num < max_value:
        largest_num = max_value
        cnt = i

print(clubs[cnt])

            
