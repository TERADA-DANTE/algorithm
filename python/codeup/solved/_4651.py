def solution(arr):
    cnt = arr.count(1)
    if cnt == 1:
        return 'C'
    if cnt == 2:
        return 'B'
    if cnt == 3:
        return 'A'
    if cnt == 4:
        return 'E'
    return 'D'


for _ in range(3):
    print(solution(list(map(int, input().split()))))
