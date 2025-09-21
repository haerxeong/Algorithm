import sys
input = sys.stdin.readline

ans = 0
s = set()

for _ in range(int(input())):
    string = input().strip()
    if string == 'ENTER':
        s = set()
    else:
        if string not in s:
            ans += 1
            s.add(string)

print(ans)