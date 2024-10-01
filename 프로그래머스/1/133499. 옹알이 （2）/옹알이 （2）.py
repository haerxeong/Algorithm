def solution(babbling):
    ans = 0
    possible = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        i = 0
        
        if "yeye" in word or "woowoo" in word or "mama" in word or "ayaaya" in word:
            i = 40
            
        while i < len(word):
            if i + 3 <= len(word) and (word[i:i+3] in possible):
                i += 3
            elif i + 2 <= len(word) and (word[i:i+2] in possible):
                i += 2
            else: i = 40    # impossible value
            
        if i < 40: ans += 1
        
    return ans