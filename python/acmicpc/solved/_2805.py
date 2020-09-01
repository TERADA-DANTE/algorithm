n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))


def cutTrees(trees, k):
    return sum([tree-k if tree-k >= 0 else 0 for tree in trees])


def solution(trees, m):
    [left, right] = [1, max(trees)]
    answer = 0
    while left <= right:
        mid = (left+right)//2
        cut = cutTrees(trees, mid)
        if cut >= m:
            answer = max(answer, mid)
            left = mid+1
        elif cut < m:
            right = mid-1
    return answer


print(solution(trees, m))
