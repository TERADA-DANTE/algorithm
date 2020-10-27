from itertools import permutations
from collections import deque
# n = int(input())
# numbers = list(map(int, input().split()))


def isValid(n, arr):
    for i in range(n):
        if arr[i] != i+1:
            return False
    return True


def answer(arr):
    if not arr:
        return '1 1' + '\n' + '1 1'
    if len(arr) == 1:
        return ' '.join(list(map(str, arr[0]))) + '\n' + '1 1'
    return ' '.join(list(map(str, arr[0]))) + '\n' + ' '.join(list(map(str, arr[1])))


def solution(n, numbers):
    queue = deque([[numbers, []]])
    while queue:
        print("queue", queue)
        arr, history = queue.popleft()
        if len(history) > 2:
            continue
        if isValid(n, arr):
            return answer(history)
        for i in range(n):
            if arr[i] != i+1:
                for j in range(n-i-1):
                    queue.append([
                        arr[:i] + list(reversed(arr[i:i+2+j])) +
                        arr[i+2+j:], history+[[i, i+2+j]]
                    ])


t = list(map(list, permutations([1, 2, 3, 4, 5], 5)))
for numbers in t:
    print(numbers)
    print(solution(5, numbers))
