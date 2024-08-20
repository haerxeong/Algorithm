#7785: 회사에 있는 사람
'''log_dict = {}
enter_list = []
n = int(input())
for i in range(n):
    input_name, log = input().split()
    log_dict[input_name] = log
    
for name in log_dict:
    if log_dict[name] == 'enter':
        enter_list.append(name)
        
for name in sorted(enter_list, reverse = True):
    print(name)'''

#14724
'''n = int(input())
clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]
largest_num, cnt = 0, 0

for i in range(9):
    num_list = list(map(int, input(": ").split()))
    if largest_num < max(num_list):
        largest_num = max(num_list)
        cnt = i

print(clubs[cnt])'''

#5586
'''string = input()
cnt_joi, cnt_ioi = 0, 0
for i in range(len(string) - 2):
    if string[i:i+3] == "JOI":
        cnt_joi += 1
    elif string[i:i+3] == "IOI":
        cnt_ioi += 1
        
print(cnt_joi)
print(cnt_ioi)'''

#3449
'''t = int(input())
for i in range(t):
    case1 = input()
    case2 = input()
    cnt = 0
    for j in range(len(case1)):
        if case1[j] != case2[j]:
            cnt += 1

    print("Hamming distance is %d." % cnt)'''

#17263
'''n = int(input())
num_list = list(map(int, input().split()))
print(max(num_list))'''

#17826
'''scores = list(map(int, input().split()))
scores.sort(reverse = True)
hongik_score = int(input())
hongik_grade = scores.index(hongik_score) + 1
if 1 <= hongik_grade <= 5:
    print("A+")
elif hongik_grade < 16:
    print("A0")
elif hongik_grade < 31:
    print("B+")
elif hongik_grade < 36:
    print("B0")
elif hongik_grade < 46:
    print("C+")
elif hongik_grade < 49:
    print("C0")
else: print("F")'''

#2153
'''alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
string = input()
cnt = 0
for s in string.lower():
    cnt += alphabets.index(s)

if cnt == 1:
    print("It is a prime word.")
else:
    for i in range(2, cnt):
        if cnt % i == 0:
            print("It is not a prime word.")
            break
        
        else:
            print("It is a prime word.")
            break'''

log_dict = {}
n = int(input())

for i in range(n):
    input_name, log = input().split()
    if log == 'enter':
        log_dict[input_name] = True

# 딕셔너리에서 키로 정렬하여 역순으로 출력
for name in sorted(log_dict.keys(), reverse=True):
    print(name)
