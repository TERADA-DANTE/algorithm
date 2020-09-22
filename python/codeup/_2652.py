n, k = list(map(int, input().split()))
total = 0
dp = [[None]*40 for _ in range(40)]


def extract(n, k):
    if n < 2*k-1:
        return 0
    elif k == 1:
        return n
    else:
        i = 2
        temp = []
        while n-i >= 2*(k-1)-1:
            temp.append([n-i, k-1])
            i += 1
        return temp


queue = [[n, k]]
while queue:
    a, b = queue.pop(0)
    q = extract(a, b)
    if isinstance(q, int):
        total += q
    else:
        queue += q
print(total)
