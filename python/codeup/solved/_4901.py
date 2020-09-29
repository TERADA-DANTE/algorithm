n = int(input())
colors = [None] + [[] for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def solution(arr, result=0):
    arr.sort()
    if len(arr) == 2:
        return abs(arr[0]-arr[1])*2
    result += abs(arr[0]-arr[1])
    result += abs(arr[-1]-arr[-2])
    for i in range(1, len(arr)-1):
        result += min(abs(arr[i]-arr[i-1]), abs(arr[i]-arr[i+1]))
    return result


for x, color in points:
    colors[color].append(x)
for color in colors:
    if color and len(color) > 1:
        answer += solution(color)
print(answer)
