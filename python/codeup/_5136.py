from collections import deque
x, y, z = list(map(int, input().split()))
d = dict({str(x)+'.'+str(y)+'.'+str(z): True})
answer = float('inf')
queue = deque([[0, x, y, z]])
while queue:
    i, x, y, z = queue.popleft()
    if x == y == z:
        print(i)
        break
    else:
        if not d.get(str(x+2)+'.'+str(y)+'.'+str(z)):
            d[str(x+2)+'.'+str(y)+'.'+str(z)] = True
            queue.append([i+1, x+2, y, z])
        if not d.get(str(x+1)+'.'+str(y+1)+'.'+str(z)):
            d[str(x+1)+'.'+str(y+1)+'.'+str(z)] = True
            queue.append([i+1, x+1, y+1, z])

        if not d.get(str(x+1)+'.'+str(y)+'.'+str(z+1)):
            d[str(x+1)+'.'+str(y)+'.'+str(z+1)] = True
            queue.append([i+1, x+1, y, z+1])

        if not d.get(str(x)+'.'+str(y+1)+'.'+str(z+1)):
            d[str(x)+'.'+str(y+1)+'.'+str(z+1)] = True
            queue.append([i+1, x, y+1, z+1])

        if not d.get(str(x)+'.'+str(y+2)+'.'+str(z)):
            d[str(x)+'.'+str(y+2)+'.'+str(z)] = True
            queue.append([i+1, x, y+2, z])

        if not d.get(str(x)+'.'+str(y)+'.'+str(z+2)):
            d[str(x)+'.'+str(y)+'.'+str(z+2)] = True
            queue.append([i+1, x, y, z+2])
