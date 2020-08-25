n, k = list(map(int, input().split()))
numbers = [None] * n
for i in range(n):
    numbers[i] = int(input())
numbers.sort()


def makeLan(numbers, mid):
    if not mid:
        return 0
    return sum([number//mid for number in numbers])


def solution(n, k):
    [left, right] = [1, numbers[-1]]
    while True:
        [l, r] = [left, right]
        mid = (left+right)//2
        s = makeLan(numbers, mid)
        if s >= k:
            left = mid
        elif s < k:
            right = mid
        if left == l and right == r:
            return max([mid+i for i in range(-5, 5) if makeLan(numbers, mid+i) >= k])


print(solution(n, k))
