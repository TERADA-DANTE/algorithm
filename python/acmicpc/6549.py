answer = []


def solution(n, heights):
    dp = [[heights[0] if heights[0] > 1 else 1, max(heights[0], 1)]]
    for i in range(1, n):
        pre, val = dp[-1]
        if pre <= heights[i]:
            dp[i] = [pre, val + pre]
        else:


while True:
    n, *heights = list(map(int, input().split()))
    if not n:
        break
    answer.append(solution(n, heights))
print(
    '\n'.join(list(map(str, answer)))
)
