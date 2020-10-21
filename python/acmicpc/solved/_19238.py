
from heapq import heappush, heappop
n, m, fuel = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]
r, c = list(map(int, input().split()))
memo = {}
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
done = [1] * m
clients = [list(map(int, input().split())) for _ in range(m)]
start = [[0] * n for _ in range(n)]
index = [[0] * n for _ in range(n)]
for i in range(m):
    start[clients[i][0]-1][clients[i][1]-1] = 1
    index[clients[i][0]-1][clients[i][1]-1] = i


def getClient(r, c):
    # 1씩 이동하면서 승객이 있느지 검사.
    isVisited = [[0] * n for _ in range(n)]
    queue = [(0, r, c)]
    client = [(float('inf'), 0, 0, 0)]
    while queue:
        f, R, C = heappop(queue)
        if start[R][C]:
            heappush(client, (f, R+1, C+1, index[R][C]))
        if len(client) < 2:
            for a, b in moves:
                row, col = R+a, C+b
                if 0 <= row < n and 0 <= col < n and not isVisited[row][col] and not board[row][col]:
                    isVisited[row][col] = True
                    heappush(queue, (f+1, row, col))
    # print(client)
    return heappop(client)


def getGoal(r, c, x, y):
    queue = [(0, r, c)]
    isVisited = [[None] * n for _ in range(n)]
    while queue:
        f, R, C = heappop(queue)
        if R == x and C == y:
            return [f, R+1, C+1]
        for a, b in moves:
            row, col = R+a, C+b
            if 0 <= row < n and 0 <= col < n and not isVisited[row][col] and not board[row][col]:
                isVisited[row][col] = True
                heappush(queue, (f+1, row, col))
    return [float('inf'), 0, 0]


def drive():
    global fuel, n, m, board, done, clients, start, r, c
    while any(done):
        distIn, r, c, idx = getClient(r-1, c-1)

        fuel -= distIn
        if fuel < 0:
            return -1
        done[idx] = 0
        start[r-1][c-1] = 0
        distOut, r, c = getGoal(
            r-1, c-1, clients[idx][2]-1, clients[idx][3]-1)
        fuel -= distOut
        if fuel < 0:
            return -1
        fuel += distOut*2
    return fuel


print(drive())
# 택시 위치에서 승객 위치까지 이동하는데, 가장 가까운애 발견하면 중단함.
# 발견못하면?
# 발견하면 그만큼 이동한 후,
# 이동못하면?
# 해당 위치에서 목적지까지 최단거리 계산
# 계산 못하면?
# 연료 소모, 소모못하면?
# 소모 한 후 연료 충전
# 모든 승객을 다 태울 때까지.
