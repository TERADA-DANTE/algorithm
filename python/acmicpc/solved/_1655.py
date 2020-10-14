import sys
input = sys.stdin.readline
n = int(input())


def solution(n):
    arr = []
    answer = []
    for i in range(n):
        arr.append(int(input()))
        j = i
        while j:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
            else:
                break

        if i % 2:
            answer.append(min(arr[(i+1)//2], arr[(i+1)//2-1]))
        else:
            answer.append(arr[(i+1)//2])
    return '\n'.join(list(map(str, answer)))


print(solution(n))
