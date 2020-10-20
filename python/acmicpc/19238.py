
from heapq import heappush, heappop
n, m, fuel = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(n)]
r, c = list(map(int, input().split()))
memo = {}
moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
done = {}
clients = []
starts = {}
for i in range(m):
    A, B, C, D = list(map(int, input().split()))
    clients.append([A, B, C, D])
    starts[f'{A-1}.{B-1}'] = str(i)


def getLine(a, b, x, y):
    queue = [(0, x, y)]
    isVisited = [[0] * n for _ in range(n)]
    isVisited[x][y] = True
    result = float('inf')
    while queue:
        f, r, c = heappop(queue)
        if r == a and c == b:
            result = min(result, f)
        for R, C in moves:
            row, col = r+R, c+C
            if 0 <= row < n and 0 <= col < n and not isVisited[row][col] and board[row][col] != 1:
                isVisited[row][col] = True
                heappush(queue, (f+1, row, col))
    return result


def getClient(r, c):
    isVisited = [[None] * n for _ in range(n)]
    queue = [(0, r, c)]
    clients = []
    while not clients and queue:
        for _ in range(len(queue)):
            cnt, R, C = heappop(queue)
            if starts.get(f'{R}.{C}'):
                heappush(clients, (cnt, R, C, starts[f'{R}.{C}']))
            for a, b in moves:
                row, col = R+a, C+b
                if 0 <= row < n and 0 <= col < n and not isVisited[row][col] and board[row][col] != 1 and not done.get(f'{row}.{col}'):
                    isVisited[row][col] = True
                    heappush(queue, (cnt+1, row, col))
    return heappop(clients)


def drive():

    global n, m, fuel, board, clients, r, c
    for _ in range(m):
        distIn, *_, index = map(int, getClient(r-1, c-1))
        fuel -= distIn
        if fuel < 0:
            return -1
        r, c = clients[index][:2]
        done[f'{r-1}.{c-1}'] = True

        distOut = getLine(clients[index][2]-1, clients[index][3]-1, r-1, c-1)
        fuel -= distOut
        if fuel < 0:
            return -1
        fuel += distOut*2
        r, c = clients[index][2:4]
    return fuel


print(drive())
