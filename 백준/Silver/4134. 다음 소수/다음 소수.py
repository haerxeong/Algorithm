def isPrime(n):
    if n <= 1: return False
    elif n <= 3: return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if not n % i: return False
        return True

for _ in range(int(input())):
    n = int(input())

    while not isPrime(n):
        n += 1

    print(n)