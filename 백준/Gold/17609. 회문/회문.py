def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def check(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                return 1
            else:
                return 2
        left += 1
        right -= 1
    return 0

for _ in range(int(input())):
    print(check(input()))