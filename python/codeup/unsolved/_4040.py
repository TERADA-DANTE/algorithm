n, m = list(map(int, input().split()))
board = [list(input()) for _ in range(n)]
s, t = list(map(int, input().split()))


def isValid(s, t):
    for i in range(s, t):
        if all([True if room == 'X' else False for room in board[i]]):
            return False
    return True

# 인덱스 주면 카운팅 후 최대값 후보 반환


def getNext(i):
    result = [None] * m
    for j in range(m):
        k = 0
        cnt = 0
        while i+k < n and board[i+k][j] == "O":
            k += 1
            cnt += 1
        result[j] = cnt
    return sorted(enumerate(result), key=lambda v: -v[1])[0]

    # 카운팅 높고, O로 존재하는 녀석


    # s ~ t 범위 내에서 옮기는 횟수가 최소가 되어야함.
if isValid(s-1, t-1):
    # 해당 날짜에서 가장 오래머물수있는 기간을 각 방마다 출력
    # 가장 큰 값으로 이동
    i = s-1
    cnt = -1
    while i < t-1:
        idx, val = getNext(i)
        i += val
        cnt += 1
    print(cnt)


else:
    print(-1)
