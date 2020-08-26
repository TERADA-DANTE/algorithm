from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
parents = [None] + [None] * n


def DFS(i, tree, parent):
    if not parents[i]:
        parents[i] = parent
        for j in tree[i]:
            DFS(j, tree, i)
    return


def solution(n):
    # 인접 리스트 생성
    arr = [None] + [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = list(map(int, input().split()))
        arr[a].append(b)
        arr[b].append(a)
    DFS(1, arr, 1)
    return '\n'.join(map(str, parents[2:]))


print(solution(n))
