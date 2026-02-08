word = input()
ans = 0
length = len(word)
i = 0

while i < length:
    if (word[i] in 'csz' and i + 1 < length and word[i + 1] == '=') or (word[i] in 'cd' and i + 1 < length and word[i + 1] == '-'):
        i += 2
    elif i + 2 < length and word[i:i+3] == 'dz=':
        i += 3
    elif word[i] in 'ln' and i + 1 < length and word[i + 1] == 'j':
        i += 2
    else:
        i += 1
    ans += 1

print(ans)