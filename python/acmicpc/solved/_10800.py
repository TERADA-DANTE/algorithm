from bisect import bisect_left as bisect
import sys
input = sys.stdin.readline

n = int(input())
balls = [[i, *list(map(int, input().split()))] for i in range(n)]


def solution(n, balls):
    balls.sort(key=lambda v: (v[2]))
    answer = [0] * n
    colors = [0] * n
    colors[balls[0][1]-1] = balls[0][2]
    acc = [0] * n
    acc[0] = balls[0][2]
    values = [value for _, _, value in balls]

    for i in range(1, n):
        index, color, value = balls[i]
        answer[index] = acc[i-1]-colors[color-1]
        j = bisect(values, value)

        for k in range(j, i):
            _, c, v = balls[k]
            if c != color:
                answer[index] -= v
        acc[i] = acc[i-1] + value
        colors[color-1] += value

    return '\n'.join(list(map(str, answer)))


print(solution(n, balls))
