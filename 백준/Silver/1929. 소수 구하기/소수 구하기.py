def isPrime(n):
    if n <= 1: return False
    elif n <= 3: return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if not n % i: return False
        return True

M, N = map(int, input().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)