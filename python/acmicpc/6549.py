answer = []


def solution(n, heights):
    dp = [[heights[0] if heights[0] > 1 else 1, max(heights[0], 1)]]
    for i in range(1, n):
        height = heights[i]
        if height >= dp[-1][0]:
            if dp[-1][1] + dp[-1][0] > height:
                result = [dp[-1][0], dp[-1][1] + dp[-1][0]]
            else:
                result = [height, height]
        else:
            l = 0
            t = height[i]
            while dp[-1-l][0] >= height:

            result = []
        dp.append()
    return 1


while True:
    n, *heights = list(map(int, input().split()))
    if not n:
        break
    answer.append(solution(n, heights))
print(
    '\n'.join(list(map(str, answer)))
)
