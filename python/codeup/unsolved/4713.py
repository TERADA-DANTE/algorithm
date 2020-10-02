from collections import deque
n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]

flowers.sort(key=lambda v: (v[0], v[1], v[2], v[3]))
print(flowers)
queue = deque(flowers)
stack = [queue.popleft()]
while queue:
    startM, startD, endM, endD = [stack[-1][i] for i in range(4)]
    sM, sD, eM, eD = q = queue.popleft()
    print(stack)
    # pre엔드보다 cur스타트가 같거나 작아야함.
    if (sM < endM or sM == endM and sD <= endD) and (endM < eM or endM == eM and endD < eD):
        if len(stack) > 1:
            preM, preD = stack[-2][2], stack[-2][3]
            if (sM < preM or sM == preM and sD <= preD) and (endM < eM or endM == eM and endD <= eD):
                stack.pop()
        stack.append(q)
print('----')
print(len(stack))
