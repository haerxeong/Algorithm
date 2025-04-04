def go(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in li:
        if not arr or arr[-1] <= i:
            arr.append(i)
            go(arr)
            arr.pop()


N, M = map(int, input().split())
li = sorted(set(map(int, input().split())))
go([])