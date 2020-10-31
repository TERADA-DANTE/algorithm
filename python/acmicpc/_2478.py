from collections import deque
n = int(input())
numbers = list(map(int, input().split()))


def isValid(n, arr):
    for i in range(n):
        if arr[i] % n != (arr[0]+i) % n:
            return False
    return True


def solution(n, numbers):
    for tail in range(n):
        queue = list(numbers)
        for i in range(n):
            if (queue[0] + i) % n != queue[i] % n:
                start, end = i, queue.index(
                    (queue[0] + i) % n if (queue[0] + i) % n else n)
                slice = queue[0:start] + \
                    list(reversed(queue[start:end+1])) + queue[end+1:]
                if isValid(n, slice):
                    head = str(n-slice.index(1))
                    body = f'{start+1} {end+1}'
                    tail = tail if tail else n
                    return head + '\n' + body + '\n' + str(tail)
        numbers.rotate(1)


print(solution(n, deque(numbers)))
