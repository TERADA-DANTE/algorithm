from collections import deque
n = int(input())
k = int(input())
lines = [list(map(int, input().split())) for _ in range(k)]


def solution(n, lines):
    # 모든 원소에 대해 BFS 실행
    # group 체크 되어있으면 플래그 끄고, 안되어있으면 플래그 켜고
    # 각 그룹을 따로 저장
    vertex = [[] for _ in range(n)]
    board = [[] for _ in range(n)]
    for a, b in lines:
        board[a-1].append(b-1)
        board[b-1].append(a-1)
    group = set()

    def BFS(i):
        queue = deque([[i, 0]])
        isVisited = [None] * n
        isVisited[i] = True
        while queue:
            q, cnt = queue.popleft()
            vertex[q].append(cnt)
            for v in board[q]:
                if not isVisited[v]:
                    isVisited[v] = True
                    queue.append([v, cnt+1])
        group.add(tuple([i for i in range(n) if isVisited[i]]))
    for i in range(n):
        BFS(i)
    result = []
    for arr in group:
        inf = float('inf')
        for i in arr:
            if inf > max(vertex[i]):
                inf = max(vertex[i])
                ret = i
        result.append(ret+1)
    return str(len(result))+'\n' + '\n'.join(list(map(str, sorted(result))))


print(solution(n, lines))
