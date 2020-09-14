
def solution(a):
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
    return [a[i] for i in range(len(a)) if not left[i] or not right[i]]


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
print(solution([9, -1, -5]))
