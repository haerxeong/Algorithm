N = int(input())  # 학생의 수
numbers = [input().strip() for _ in range(N)]  # 학생 번호 리스트

# 뒤에서부터 몇 자리를 확인할 것인지
for k in range(1, len(numbers[0]) + 1):
    suffixes = set()  # 뒤에서 k자리를 자른 번호를 저장할 집합
    for number in numbers:
        suffix = number[-k:]  # 뒤에서 k자리를 자른 부분
        suffixes.add(suffix)  # 집합에 추가 (중복이 자동으로 처리됨)
    
    # 모든 번호의 뒤 k자리 부분이 고유하면 k가 답
    if len(suffixes) == N:
        print(k)
        break