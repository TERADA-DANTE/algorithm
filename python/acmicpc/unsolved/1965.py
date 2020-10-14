n = int(input())


def solution(n):
    boxes = list(map(int, input().split()))
    dp = [0]*n
    for i in range(n):
        if i:
            m = [dp[j]
                 for j in range(0, i) if boxes[j] < boxes[i]]
            dp[i] = max(m)+1 if m else 0
    return max(dp)+1


print(solution(n))
