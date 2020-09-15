
def solution(a):
    cnt = 0
    l = len(a)
    left, right = [0] * l, [0] * l
    for i in range(l - 2, -1, -1):
        for j in range(i, l):
            if a[i] > a[j]:
                left[i] = left[j] + 1
                break
    for i in range(1, l):
        for j in range(i-1, -1, -1):
            if a[i] > a[j]:
                right[i] = right[j] + 1
                break
    for i in range(l):
        if left[i] * right[i] == 0:
            cnt += 1
    return cnt


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
print(solution([9, -1, -5]))
