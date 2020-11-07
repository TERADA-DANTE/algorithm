n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]


def solution(n, m, arr):
    a, b = list(map(int, input().split()))
    floors = [float('inf')]*100
    for start, step in arr:
        for i in range(int((100-start)/step)):
            floors[start+step*i] = min(floors[start+step*i], i)
    return list(enumerate(floors))


print(solution(n, m, arr))
