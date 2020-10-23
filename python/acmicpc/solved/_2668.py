from collections import deque
n = int(input())
numbers = [-1] + [int(input()) for _ in range(n)]
cycles = []
# 사이클의 개수
# dfs로 각 원소를 돈다.
# 사이클을 이루는 것을 반환한다.
answer = []


def solution():
    # 큐로 생각?
    def dfs(queue, initial):
        isVisited = []
        while queue:
            q = queue.popleft()
            isVisited.append(q)
            if q in cycles:
                continue
            elif numbers[q] not in isVisited:
                queue.append(numbers[q])
            elif numbers[q] == initial:
                for number in isVisited:
                    cycles.append(number)
                return isVisited

    for i in range(1, n+1):
        dfs(deque([i]), i)
    return '\n'.join(list(map(str, [len(cycles), *sorted(cycles)])))


print(solution())
