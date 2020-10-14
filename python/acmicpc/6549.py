
def solution(h):
    mid = min(h) * len(h)
    left = h[0:int(len(h)//2)] if h[0:int(len(h)//2)] else 0
    right = h[int(len(h)//2):] if h[int(len(h)//2):] else 0
    print(h, left, right)
    if len(left) == 1:
        left = left[0]
    else:
        left = solution(left)
    if len(right) == 1:
        right = right[0]
    else:
        right = solution(right)
    print('max', max(mid, left, right), 'in', left, mid, right)
    return max(mid, left, right)


while True:
    inputs = list(map(int, input().split()))
    if not inputs[0]:
        break
    n, *h = inputs
    print(solution(h))
