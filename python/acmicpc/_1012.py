from collections import deque


def solution(width, height, n, board):
    cnt = 0
    isVisited = [[0] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            # 방문하지 않았다면
            if not isVisited[i][j]:
                isVisited[i][j] = True
                # 해당 구역이 배추가 심어져있다면
                if board[i][j]:
                    # 지렁이를 심는다.
                    cnt += 1
                    # 지렁이가 갈 수 있는 곳은 다 방문해준다.
                    queue = deque([[i, j]])

                    while queue:
                        r, c = queue.popleft()
                        for row, col in moves:
                            x, y = r+row, c+col
                            if 0 <= x < height and 0 <= y < width and not isVisited[x][y] and board[x][y]:
                                isVisited[x][y] = True
                                queue.append([x, y])
    return cnt
    # 연속된 1의 위치의 개수
    # 같은 크기의 방문여부 배열 생성
    # 모든 배열을 도는데, 방문했던 곳은 안돌아도됨.
    # 1을 발견하면 카운트를 증가시키고 갈 수 있는 곳은 다 가면서
    # 방문체크를 한다.


for _ in range(int(input())):
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    m, n, k = list(map(int, input().split()))
    board = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        col, row = list(map(int, input().split()))
        board[row][col] = 1
    print(solution(m, n, k, board))
