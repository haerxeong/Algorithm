for _ in range(int(input())):
    ans = 0
    now = 1

    string = input()
    for s in string:
        if s == 'X':
            now = 1
        else:
            ans += now
            now += 1

    print(ans)