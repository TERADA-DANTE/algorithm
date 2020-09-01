from collections import deque
lim, cur, des, u, d = list(map(int, input().split()))


def solution(lim, cur, des, u, d, cnt=0):
    isVisited = dict()
    queue = deque([[0, cur]])
    while queue:
        l = len(queue)
        for _ in range(l):
            cnt, val = queue.popleft()
            if val == des:
                return cnt
            if not isVisited.get(val):
                isVisited[val] = True
                next = []
                if val + u <= lim:
                    next.append([cnt+1, val+u])
                if val-d > 0:
                    next.append([cnt+1, val-d])
                queue += next
    return 'use the stairs'


print(solution(lim, cur, des, u, d))
