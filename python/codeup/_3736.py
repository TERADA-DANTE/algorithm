n = int(input())
numbers = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
a = [0]


def find(n):
    l, r = 0, len(a)
    while l < r:
        mid = int((l+r)//2)
        if n > a[mid]:
            l = mid+1
        else:
            r = mid
    return r


for i in range(1, n+1):
    if numbers[i] > a[-1]:
        dp[i] = dp[i-1]+1
        a.append(numbers[i])
    else:
        # a 에서 numbers[i] 의 위치를 찾는다.
        index = find(numbers[i])

        a[index] = min(numbers[i], a[index])
        dp[i] = dp[index-1] + 1
print(len(a)-1)
