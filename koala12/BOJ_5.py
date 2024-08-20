#11005: 진법변환2
'''dic = {}
output = []

for i in range(10):
    dic[i] = str(i) #join으로 출력하기 위해 str로 변환
for i in range(10, 36):
    dic[i] = chr(i + 55)
    
n, b = map(int, input().split())

while True:
    if n == 0: break
        
    else:
        output.append(dic[n % b])
        n //= b
        
print(''.join(output[::-1]))'''

#12174: #include <Google I/O.h>
'''t = int(input())

for i in range(t):
    input_byte = int(input())
    string = input()
    bin_list = [] #bin_list는 input_byte만큼의 요소를 가짐
    output = ''

    for j in range(0, len(string), 8): #I, O를 1, 0으로 바꾸고 8자씩 bin_list에 넣는 과정. 
        x = ''
        for s in string[j : j + 8]:
            if s == 'I':
                x += '1'
            elif s == 'O': 
                x += '0'
        bin_list.append(x)

    for j in range(input_byte):
        output += chr(int(bin_list[j], 2))

    print("Case #%d: %s" % (i + 1, output))'''
            
#2745: 진법변환_koala
'''n, b = input().split()
b = int(b)

dic = {}

for i in range(36):
    if i < 10:
        dic[str(i)] = i
    else:
        dic[chr(i + 55)] = i

ans = 0

for i in range(len(n)):
    ans += dic[n[i]] * (b ** (len(n) - i - 1))

print(ans)'''

#14915: 진수 변환기
'''int_m, n = map(int, input().split())
dic = {}
ans = []

for i in range(16):
    if i < 10:
        dic[i] = str(i)
    else:
        dic[i] = chr(i + 55)

while True:
    if int_m == 0:
        if len(ans) == 0: #0도 포함한 거 진짜 개열받고 더럽고 치사함
            print(int_m)

        break

    ans.append(dic[int_m % n])
    int_m //= n
    
print(''.join(ans[::-1]))'''

#11179: 2진수 뒤집기
'''n = int(input())
bin_str = ''
ans = 0

while n != 0:
    bin_str += str(n % 2)
    n //= 2

for i in range(len(bin_str)):
    ans += int(bin_str[i]) * (2 ** (len(bin_str) - 1 - i))

print(ans)'''

#13235: 팰린드롬
'''input_word = input()
flag = True

for i in range(len(input_word) // 2):
    if input_word[i] != input_word[len(input_word) - i - 1]:
        flag = False
        break

if flag:
    print('true')

else:
    print('false')'''

#11068: 회문인 수 tqtqtq나중에다시지우고머리비우고풀어
'''def converse(n, b):
    ans = []
    while n > 0:
        ans.append(n % b)
        n //= b
    return ans[::-1]

def is_palindrome(text):
    for i in range(len(text) // 2):
        if text[i] != text[- 1 - i]:
            return False
    return True

t = int(input())

for i in range(t):
    input_int = int(input())
    flag = False

    for j in range(2, 65):
        if is_palindrome(converse(input_int, j)):
            flag = is_palindrome(converse(input_int, j))
            break

    print(int(flag))'''

#3062: 수 뒤집기
'''t = int(input())
for i in range(t):
    n = input()
    reverse_n = n[::-1]
    val = str(int(n) + int(reverse_n))

    flag = True
    for j in range(len(val) // 2):
        if val[j] != val[- 1 - j]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")'''

#17502: 클레어와 팰린드롬 #하... 내코드 이거 레전드로 긴데? 좀 수정해봐봐
'''n = int(input())
string = input()

if n == 1:
    if string != '?':
        print(string)

    else:
        print('a')

else:
    ans = ['a'] * n

    for i in range(n // 2):
        if string[i] == string[- 1 - i] == '?':
            ans[i] = ans[- 1 - i] = 'a'
        
        elif string[i] == '?':
            ans[i] = ans[- 1 - i] = string[- 1 - i]

        elif 'a' <= string[i] <= 'z':
            ans[i] = ans[- 1 - i] = string[i]

    if n % 2 == 1 and string[n // 2] != '?':
        ans[n // 2] = string[n // 2]

    print(''.join(ans))'''

#14561: 회문
'''dic = {}
for i in range(16):
    if i < 10:
        dic[i] = str(i)
    else:
        dic[i] = chr(i + 55)

t = int(input())
for i in range(t):
    int_a , base = map(int, input().split())
    ans = []

    while int_a > 0:
        ans.append(dic[int_a % base])
        int_a //= base

    ans = ''.join(ans[::-1])
    flag = True
    for j in range(len(ans) // 2):
        if ans[j] != ans[- j - 1]:
            flag = False

    print(int(flag))'''

#10828: 스택
'''import sys 
input = sys.stdin. readline

stack = []
n = int(input())
for i in range(n):
    input_list = list(input().split())

    if input_list[0] == 'push':
        stack.append(input_list[1])

    elif input_list[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    elif input_list[0] == 'size':
        print(len(stack))

    elif input_list[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else: print(0)

    elif input_list[0] == 'top':
        if len(stack) > 0:
            print(stack[-1])
        else: 
            print(-1)'''

#3996: 좋은 단어
'''n = int(input())
ans = 0
for i in range(n):
    stack = []
    text = input()
    for j in range(len(text)):
        if len(stack) == 0:
            stack.append(text[j])
        else:
            if stack[-1] == text[j]:
                stack.pop()
            else:
                stack.append(text[j])
    if len(stack) == 0:
        ans += 1
print(ans)'''


#1874: 스택 수열
'''n = int(input())
for _ in range(n):
    d = int(input())
''' #시발... 제가 공부를 안 하는 게 아닙니다... 존나 어려워서 못하는 겁니다...

'''cnt = 1
flag = True
stack = []
op = []

n = int(input())
for i in range(n):
    num = int(input())
    
    while cnt <= num:
        stack.append(cnt)
        op.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        op.append('-')
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in op:
        print(i)''' #...좀베꼈어요

#10773: 제로
'''k = int(input())
stack = []

for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else: stack.pop()

print(sum(stack))'''

#4949: 균형잡힌 세상
'''while 1:
    string = input()
    if string == '.':
        break
    stack = []

    for s in string:
        if s != "[" and s != "]" and s != "(" and s != ")":
            continue

        if len(stack) == 0:
            stack.append(s)
        else:
            if (s == ")" and stack[-1] == "(") or (s == "]" and stack[-1] == "["):
                stack.pop()
            else:
                stack.append(s)
    if len(stack) == 0:
        print("yes")
    else: print("no")'''

#2596: 비밀편지
'''n = int(input())
input_string = input()
input_list = [input_string[i : i + 6] for i in range(0, len(input_string), 6)]

dic = {"A" : "000000", "B" : "001111", "C" : "010011", "D" : "011100", 
        "E" : "100110", "F" : "101001", "G" : "110101", "H" : "111010"}

code = list(dic.values())
ans = ''

for i in range(n):
    if input_list[i] in code:
        ans += chr(65 + code.index(input_list[i]))
    else:
        temp = ''
        for j in range(8): #a~h 반복 비교
            cnt = 0
            for k in range(6): #각글자
                if code[j][k] != input_list[i][k]: 
                    cnt += 1
            if cnt == 1: 
                temp += chr(j + 65)

        if len(temp) > 1 or len(temp) == 0:
            ans = i + 1
            break
        else: ans += temp
print(ans)''' #나이거ㅍ풀었다나진짜짱이다

#1316: 그룹 단어 체커
'''n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    arr = []
    flag = True
    for i in range(len(word)):
        if word[i] not in arr:
            arr.append(word[i])
        else:
            if arr[-1] != word[i]:
                flag = False
                break

    if flag: cnt += 1

print(cnt)'''

#2789: 유학 금지
'''for s in input():
    if s  not in 'CAMBRIDGE':
        print(s, end = '')'''

#14582: 오늘도 졌다
'''scores1 = list(map(int, input().split()))
scores2 = list(map(int, input().split()))
sum1, sum2, flag = 0, 0, False

for i in range(9):
    sum1 += scores1[i]
    if sum1 > sum2:
        flag = True
    sum2 += scores2[i]

if flag: print("Yes")
else: print("No")'''

#7510: 고급 수학
'''n = int(input())
for i in range(n):
    sides = list(map(int, input().split()))

    print("Scenario #%d:" % (i + 1))
    sides.sort()

    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        print("yes\n")
    else: print("no\n")'''

#13410: 거꾸로 구구단
'''n, k = map(int, input().split())
arr = []

for i in range(1, k + 1):
    val = str(n * i)[::-1]
    arr.append(int(val))

print(max(arr))'''

#11652: 카드
'''n = int(input())
dic = {}
ans = []
for _ in range(n):
    d = int(input())
    if d in dic:
        dic[d] += 1
    else: dic[d] = 1

max_cnt = max(list(dic.values()))

for key, value in dic.items():
    if value == max_cnt:
        ans.append(key)

print(sorted(ans)[0])'''

#11728: 배열 합치기
'''input = __import__('sys').stdin.readline
m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
arr = tuple(sorted(a + b))
print(' '.join(map(str, arr)))'''

#