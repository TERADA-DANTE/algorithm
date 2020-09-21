n, k = list(map(int, input().split()))
total = 0

queue = [[n, k]]

while queue:
    print(queue)
    m, l = queue.pop(0)
    if l == 1:
        total += m
    elif m >= 2*l-1:
        i = 2
        while m-i >= l:
            queue.append([m-i, l-1])
            i += 1
print(total)
