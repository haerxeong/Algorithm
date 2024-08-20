#9226: 도깨비말
'''vowels = 'aeiou'

while True:
    string = input()
    if string == '#':
        break
        
    else:
        if string[0] in vowels:
            print(string + 'ay')
        else:
            has_vowel = False
            for i in range(len(string)):
                if string[i] in vowels:
                    print(string[i:] + string[:i] + 'ay')
                    has_vowel = True
                    break
            if not has_vowel:
                print(string + 'ay')'''

#1159: 농구 경기
'''n = int(input())
last_names = []
name_set = set()

trueorfalse = True

if n < 5:
    trueorfalse = False

for i in range(n):
    last_names.append(input())

last_names.sort()

for i in range(n - 4):
    if last_names[i][0] == last_names[i + 4][0]:
        name_set.add(last_names[i][0])

if len(name_set) == 0:
    trueorfalse = False

if trueorfalse:
    for s in sorted(name_set):
        print(s, end = '')
else:
    print("PREDAJA")'''
    
#3181: 줄임말 만들기
'''string_list = list(input().split())
remove_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
initialisms = []

if string_list[0] in remove_list:
    initialisms.append(string_list[0][0])

for _ in remove_list:
    if _ in string_list:
        string_list.remove(_)

for s in string_list:
    initialisms.append(s[0])

for s in initialisms:
    print(s.upper(), end = '')'''

#6996: 애너그램
'''t = int(input())

for i in range(t):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print("%s & %s are anagrams." % (a, b))
    else: print("%s & %s are NOT anagrams." % (a, b))'''

#1302: 베스트셀러
'''books = []
n = int(input())
for i in range(n):
    books.append(input())

book_set = set(books)

cnt = 0
book_name = []

for name in book_set:
    if books.count(name) > cnt:
        cnt = books.count(name)
        book_name.clear()
        book_name.append(name)
    elif books.count(name) == cnt:
        book_name.append(name)

book_name.sort()
print(book_name[0])'''

#5218: 알파벳 거리
'''t = int(input())
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(t):
    x, y = input().split()

    print("Distances:", end = ' ')

    for j in range(len(x)):
        if alphabets.index(x[j]) > alphabets.index(y[j]):
            distance = alphabets.index(y[j]) + 26 - alphabets.index(x[j])
        else:
            distance = alphabets.index(y[j]) - alphabets.index(x[j])
        print(distance, end = ' ')
    print()'''

#15813: 너의 이름은 몇 점이니?
'''alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
name_len = int(input())
name = input()

cnt = 0

for s in name:
    cnt += alphabets.index(s) + 1

print(cnt)'''

#3059: 등장하지 않는 문자의 합
'''t = int(input())
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(t):
    text = input()
    find_non = list(alphabets)

    for s in text:
        if s in find_non:
            find_non.remove(s)

    cnt = 0
    for s in find_non:
        cnt += alphabets.index(s) + 65

    print(cnt)'''

#1157: 단어 공부
'''input_word = input()
input_word = input_word.upper()
word_set = set(input_word)

cnt = 0
most_alphabet = []

for s in word_set:
	if cnt < input_word.count(s):
		cnt = input_word.count(s)
		most_alphabet.clear()
		most_alphabet.append(s)

	elif cnt == input_word.count(s):
		most_alphabet.append(s)

if len(most_alphabet) > 1:
	print("?")
else:
	print(most_alphabet[0])'''

#11718: 그대로 출력하기
'''while True:
    try: 
        print(input())
    except EOFError: #이게뭔데 ㅋㅋ
        break'''

#10823: 더하기 2
'''string = ''
while True:
    try:
        string += input()
    except EOFError:
        break

num_list = map(int, string.split(','))
print(sum(num_list))'''

#1371: 가장 많은 글자 _아스키코드를 써보아요...
'''asc_list = [0] * 26
input_string = ''

while True:
    try:
        input_string += input()
    except EOFError:
        break

for s in input_string:
    if s != ' ':
        asc_list[ord(s) - 97] += 1

print_list = []

for i in range(26):
    if asc_list[i] == max(asc_list):
        print_list.append(chr(i + 97))

for s in sorted(print_list):
    print(s, end = '')'''

#1673: 치킨 쿠폰
# k * stamp = n
while True:
    try:
        n, k = map(int, input().split())
        order = n + (n // k)
        
        while n >= k:
            n = (n // k) + (n % k)
            order += n // k

        print(order) 

    except EOFError:
        break  ########진짜이해가안되네

#6502: 동혁 피자
'''i = 1
while True:
    try:
        r, w, l = map(int, input().split())

        if (0.5 * w) ** 2 + (0.5 * l) ** 2 <= r ** 2:
            print("Pizza %d fits on the table." % i)
        else: 
            print("Pizza %d does not fit on the table." % i)
        
        i += 1

    except ValueError:
        break'''

#1362: 펫 (blog)
'''i = 1

while True:
    o, w = map(int, input().split())
    if o == w == 0: 
        break

    while True:
        action, n = input().split()
        n = int(n)

        if action == '#' and n == 0: 
            break

        if w > 0:
            if action == 'F':
                w += n
            elif action == 'E':
                w -= n

    if o * 0.5 < w < o * 2:
        print(i, ":-)")

    elif w <= 0:
        print(i, "RIP")

    else: print(i, ":-(")

    i += 1'''

#16205: 변수명
'''case_num, variable_n = input().split()
case_num = int(case_num)

word_list = []

def camel_pascal(i):
    global variable_n
    while i < len(variable_n): 
        if ord('A') <= ord(variable_n[i]) <= ord('Z'):
            word_list.append(variable_n[:i])
            variable_n = variable_n[i:]
            i = 1
        else:
            i += 1
    if variable_n:
        word_list.append(variable_n)

if case_num == 1:
    camel_pascal(0)

    print(*word_list, sep = '')
    print('_'.join([s.lower() for s in word_list]))
    print(''.join([s.title() for s in word_list]))

elif case_num == 2:
    word_list = list(variable_n.split('_'))

    print(word_list[0] + ''.join([s.title() for s in word_list[1:]]))
    print(variable_n)
    print(''.join([s.title() for s in word_list]))

elif case_num == 3:
    camel_pascal(1)

    print(word_list[0].lower() + ''.join(word_list[1:]))
    print('_'.join([s.lower() for s in word_list]))
    print(*word_list, sep = '')'''

#14935: FA
'''x = input()

def FA(x):
    x1 = x[0]
    x2 = len(x)
    new_x = str(int(x1) * int(x2))
    if x != new_x:
        return FA(new_x)
    else:
        print("FA")
    return new_x

FA(x)'''

#2495: 연속구간
'''for _ in range(3):
    i = input()
    len_max = 0
    cnt = 1
    for j in range(7): 
        if i[j] == i[j + 1]:
            cnt += 1
        else:
            cnt = 1

        if len_max < cnt:
            len_max = cnt
    print(len_max)'''

#3985: 롤케이크
'''l = int(input())
n = int(input())

cake_list = [0] * l
expected = 0
expected_guest = 0

for i in range(1, n + 1):
    p, k = map(int, input().split())

    if k - p > expected:
        expected = k - p
        expected_guest = i
    
    for j in range(p - 1, k):
        if cake_list[j] == 0:
            cake_list[j] = i

cnt = 0
max_guest = 0
for k in range(1, n + 1):
    if cake_list.count(k) > cnt:
        cnt = cake_list.count(k)
        max_guest = k

print(expected_guest)
print(max_guest)'''

#2828: 사과 담기 게임 ######전혀모르겟누...
'''n, m = map(int, input().split())
j = int(input()) 

left = 1
right = m
dis = 0

for i in range(j):
    location = int(input())
    
    if left <= location <= right:
        continue

    if left > location:
        dis += left - location
        right -= left - location
        left = location

    else: 
        dis += location - right
        left += location - right
        right = location

print(dis)'''

#2947: 나무 조각
'''n_list = list(map(int, input().split()))

while n_list != [1, 2, 3, 4, 5]:
    for i in range(4):
        if n_list[i] > n_list[i + 1]:
            n_list[i], n_list[i + 1] = n_list[i + 1], n_list[i]
            print(*n_list, sep = ' ')'''