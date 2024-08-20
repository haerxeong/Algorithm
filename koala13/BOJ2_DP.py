#9465: 스티커
'''for i in range(int(input())):
    n = int(input())
    stikers = [list(map(int, input().split())) for _ in range(2)]
    ''' #너무어려워요

#11053: 가장 긴 증가하는 부분 수열
'''n = int(input())
series = list(map(int, input().split()))
cnt = 1; arr = [series[0]]
for i in range(1, n):
    if arr[-1] < series[i]: 
        arr.append(series[i])
print(len(arr))
print(*arr)'''

