for _ in range(int(input())):
    cent = int(input())
    quarter = cent // 25
    dime = (cent % 25) // 10
    nickel = (cent % 25 % 10) // 5
    penny = cent % 25 % 10 % 5
    print(quarter, dime, nickel, penny)