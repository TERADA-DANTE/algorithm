n = int(input())
numbers = list(enumerate(list(map(int, input().split())), start=1))
numbers.sort(key=lambda v: v[1])
m = int(input())
questions = list(map(int, input().split()))


def reply(q):
    l, r = 0, n
    while l < r:
        mid = int((l+r)//2)
        if numbers[mid][1] < q:
            l = mid+1
        elif q < numbers[mid][1]:
            r = mid-1
        else:
            return numbers[mid][0]
    if r < n and numbers[r][1] == q:
        return numbers[r][0]
    else:
        return -1


print(*[reply(question) for question in questions])
