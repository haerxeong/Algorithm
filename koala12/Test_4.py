#1436: 영화감독 숌
'''n = int(input())

cnt = 0
x = 666

while True:
    if '666' in str(x):
        cnt += 1
    
    if n == cnt:
        print(x)
        break
    
    x += 1'''

#1813: 논리학 교수
'''n = int(input())
int_list = list(map(int, input().split()))
true_list = []

for i in int_list:
    if int_list.count(i) == i:
        true_list.append(i)

if len(true_list) != 0:
    print(max(true_list))''' #모르겟고연..

#2153: 소수단어
'''word = input()

cnt = 0
for s in word:
    if 'a' <= s <= 'z':
        cnt += (ord(s) - ord('a') + 1)

    elif 'A' <= s <= 'Z':
        cnt += (ord(s) - ord('A') + 27)

prime = True
for i in range(2, int(cnt ** 0.5) + 1): #소수 판별에서 왜 제곱근이 사용되는지 모르겠네 (-> 약수가 제곱근을 기준으로 대칭이므로!!! 제곱근까지만 확인하면 됨!!)
    if cnt % i == 0:
        prime = False

if prime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")'''

#1051: 숫자 정사각형
'''n, m = map(int, input().split())

for i in range(n):
    rect = list(int(input()))

square_len = 0
i = 2
if n >= m:
    while i < m:
        for j in range()

if square_len == 0:
    square_len = 1 ''' #####하또뇌정지..
