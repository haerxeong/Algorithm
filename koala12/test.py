'''#2748
n = int(input())

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(5)''' #피보나치 구현하는 법.
############
'''n = int(input())
f1 = [1]; f2 = [2, 3]; arr = []

def fibo(n):
    if n == 1:
        return f1
    elif n == 2:
        return f2
    else:
        return fibo(n-1) + fibo(n-2)'''
##############
n = int(input())
cnt = 3
f1 = [1]
f2 = [2,3]
if n == 1: print(*f1)
elif n == 2: print(*f2)
else:
    while cnt <= n:
        arr = []
        for i in f1:
            arr.append(i + 2 ** (cnt - 1))

        for i in f2:
            arr.append(i + 2 ** (cnt - 1))

        if cnt == n:
            break
        else:
            cnt += 1
            f1 = f2
            f2 = arr
        
    print(*arr)

#############내가해냄
