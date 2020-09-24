from collections import deque
a, b, c, d = list(map(int, input().split()))
check = dict({'0.0': True})

# q : cnt, l, r
queue = deque([[0, 0, 0]])
while queue:
    cnt, l, r = queue.popleft()
    if l == c and r == d:
        print(cnt)
        queue.append('.')
        break
    # 왼버림
    if not check.get('0.'+str(r)):
        check['0.'+str(r)] = True
        queue.append([cnt+1, 0, r])
    # 오른버림
    if not check.get(str(l)+'.0'):
        check[str(l)+'.0'] = True
        queue.append([cnt+1, l, 0])
    # 왼채움
    if not check.get(str(a)+'.'+str(r)):
        check[str(a)+'.'+str(r)] = True
        queue.append([cnt+1, a, r])
    # 오른채움
    if not check.get(str(l)+'.' + str(b)):
        check[str(l)+'.' + str(b)] = True
        queue.append([cnt+1, l, b])
    # 오른쪽 이동
    if l <= b-r:
        if not check.get('0.' + str(r+l)):
            check['0.' + str(b-r+l)] = True
            queue.append([cnt+1, 0, r+l])
    else:
        if not check.get(str(l-b+r) + '.' + str(b)):
            check[str(l-b+r) + '.' + str(b)] = True
            queue.append([cnt+1, l-b+r, b])
    # 왼쪽 이동
    if a-l >= r:
        if not check.get(str(l+r)+'.0'):
            check[str(l+r)+'.0'] = True
            queue.append([cnt+1, l+r, 0])
    else:
        if not check.get(str(a) + '.' + str(r-a+l)):
            check[str(a) + '.' + str(r-a+l)] = True
            queue.append([cnt+1, a, r-a+l])

        # 2 5 2 4 => 5
        # 3 7 3 2 => 9
if not queue:
    print(-1)
