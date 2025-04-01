switch_num = int(input())
switches = list(map(int, input().split()))

for _ in range(int(input())):
    gender, num = map(int, input().split())

    if gender == 1:  # 남자
        for i in range(num - 1, switch_num, num):
            switches[i] ^= 1

    else: # 여자
        switches[num - 1] ^= 1
        left, right = num - 2, num

        while 0 <= left < right < switch_num and switches[left] == switches[right]:
            switches[left] ^= 1
            switches[right] ^= 1
            left -= 1
            right += 1

for i in range(switch_num):
    print(switches[i], end = ' ')
    if i % 20 == 19: print()