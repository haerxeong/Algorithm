#DP #그리디도 해보기
#9465번: 스티커
f'''or _ in range(int(input())):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(2)] 
    for i in range(1, n):
        if i == 1:
            li[0][1] += li[1][0] #s[0][j] += s[1][j - 1]
            li[1][1] += li[0][0] #s[1][j] += s[0][j - 1]
        else:
            li[0][i] += max(li[1][i - 1], li[1][i - 2])
            li[1][i] += max(li[0][i - 1], li[0][i - 2])
    print(max(li[0][n - 1], li[1][n - 1]))'''

#14916번: 거스름돈_그리디
'''n = int(input())
cnt = 0
while n > 0:
    if n % 5 == 0:
        print(cnt + n // 5)
        break
    n -= 2
    cnt += 1

    if n == 0: print(cnt)
    elif n < 0: print(-1)'''

    #DP
'''n = int(input())
li = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 2 or i == 5:
        li[i] = 1
    elif i > 3:
        if li[i - 2] and li[i - 5]:
            li[i] = 1 + min(li[i - 2], li[i - 5])
        elif li[i - 2]:
            li[i] =  1 + li[i - 2]
        elif li[i - 5]:
            li[i] = 1 + li[i - 5]
            
print(li[n] if li[n] else -1)'''

#16395번: 파스칼의 삼각형
'''n, k = map(int, input().split())

C = [[0] * (i + 1) for i in range(n + 1)]
C[0][0], C[1][0], C[1][1] = 1, 1, 1

for i in range(2, n):
    for j in range(i + 1):
        if j == 0 or j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

print(C[n - 1][k - 1])'''

#14495번: 피보나치 비스무리한 수열
'''n = int(input())
li = [0] * (n + 1)

for i in range(1, n + 1):
    if i in [1, 2, 3]:
        li[i] = 1
    else:
        li[i] = li[i - 1] + li[i - 3]

print(li[n])'''

#15642번: 피보나치 수 7
'''import sys     
sys.setrecursionlimit(10000)

def fibo(n):
    if n == 0: return f[0]
    if f[n]: return f[n]

    f[n] = fibo(n - 1) + fibo(n - 2)
    return f[n]

n = int(input())
f = [0] * (n + 1)
f[1] = 1

print(fibo(n) % 1000000007)'''

'''n = int(input())
f = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        f[i] = 1
    else:
        f[i] = f[i - 1] + f[i - 2]
        f[i] %= 1000000007

print(f[n])'''

#1463번: 1로 만들기
'''import sys     
sys.setrecursionlimit(10000000)

def DP(n):
    if n == 2 or n == 3: return 1
    if dp[n]: return dp[n]

    dp[n] = DP(n - 1)
    if n % 3 == 0: dp[n] = min(dp[n], DP(n//3))
    if n % 2 == 0: dp[n] = min(dp[n], DP(n//2))
    dp[n] += 1

    return dp[n]

N = int(input())
dp = [0] * (N + 1)
print(DP(N))'''


'''N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1):
    if i == 2 or i == 3:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1]

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2])
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3])
        dp[i] += 1

print(dp[N])'''

#17626번: Four Squares
'''n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if (i**0.5)**2 == i:
        dp[i] = 1
    else:
        
        '''

#11726번: 2xn 타일링
#결국 1과 2로 n을 만드는 경우의 수와 같은 거 같은데요...
'''n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else: 
        dp[i] = dp[i - 2] + dp[i - 1]
    
    dp[i] %= 10007
        
print(dp[n])'''
    
#14501번: 퇴사
'''N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    t = li[i][0]
    if t + i < N:
        dp[i + t] += li[i][1]

print(max(dp))
print(dp)'''
#retry
'''N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N
max_dp = 0

for i in range(N):
    for j in range(i):
        if j + li[j][0] <= i:
            max_dp = max(dp[i], li[j][1])
    dp[i] += max_dp

print(max(dp))
print(dp)  '''      
#reretry
'''def DP(n):
    if n + li[n][0] >= N:
        return 0
    else:
        dp[n] = li[n][1] + DP(li[n][0] + n)

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i + li[0][0] < N:
        DP(i)

print(max(dp))
print(dp)'''

#11053번: 가장 긴 증가하는 부분 수열
'''
N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    
print(max(dp))
'''

#11055번: 가장 큰 증가하는 부분 수열
'''N = int(input())
A = list(map(int, input().split()))
dp = [A[i] for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + A[i])

print(max(dp))'''

#1965번: 상자 넣기
'''n = int(input())
box = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))'''

#11722: 가장 긴 감소하는 부분순열
'''N = int(input())
A = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[i], 1 + dp[j])
print(max(dp))
'''

#1309번: 동물원
'''N = int(input())
dp = [1] * (N)

for i in range(N):
    if i == 0:
        dp[i] = 3
    elif i == 1:
        dp[i] = 7
    else:
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % 9901

print(dp[N - 1])'''

#9251번: LCS
'''s1 = list(input())
s2 = list(input())

for i in range(len(s2)):
    if s2[i] == s1[0]: s2 = s2[i::]

for s in s1:
    if s '''