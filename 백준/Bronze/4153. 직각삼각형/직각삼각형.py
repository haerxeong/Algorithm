while True:
    a, b, c = sorted(map(int, input().split()))
    if not a and not b and not c: break
    print("right" if a*a + b*b == c*c else "wrong")