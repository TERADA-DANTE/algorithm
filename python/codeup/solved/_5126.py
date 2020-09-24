from collections import deque
plates = list(map(int, input().split()))


def isValid(arr):
    if not any(arr):
        return True
    return False


def convert(arr, i):
    if i == 0:
        return [0 if arr[0] else 1] + [0 if arr[1] else 1] + arr[2:]
    elif i == 7:
        return arr[:6] + [0 if arr[6] else 1] + [0 if arr[7] else 1]
    else:
        return arr[:i-1] + [0 if arr[i-1] else 1] + [0 if arr[i] else 1] + [0 if arr[i+1] else 1] + arr[i+2:]


queue = deque([[0, plates]])
while queue:
    i, q = queue.popleft()
    if isValid(q):
        print(i)
        break
    else:
        for j in range(8):
            queue.append([i+1, convert(q, j)])
