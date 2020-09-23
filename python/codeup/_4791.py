m, n, l = list(map(int, input().split()))
shooters = sorted(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(n)]
cnt = 0


def search(i):
    if i <= shooters[0]:
        return shooters[0]
    elif shooters[-1] <= i:
        return shooters[-1]
    else:
        l, r = 0, m
        while abs(l-r) > 1:
            mid = int((l+r)//2)
            if shooters[mid] < i:
                l = mid
            elif i < shooters[mid]:
                r = mid
            else:
                return shooters[mid]
        return shooters[l] if abs(shooters[l] - i) < abs(shooters[r] - i) else shooters[r]


for x, y in animals:
    if l >= abs(search(x) - x) + y:
        cnt += 1
print(cnt)
