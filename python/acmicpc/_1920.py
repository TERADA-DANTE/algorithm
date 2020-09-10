n = int(input())
arr = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))


def solution(n, m, arr, numbers):
    answer = []
    for number in numbers:
        l = 0
        r = n-1
        while l < r:
            mid = int((l+r)//2)
            if arr[mid] == number:
                break
            if arr[mid] < number:
                l = mid+1
            else:
                r = mid-1
        if arr[r] == number or arr[mid] == number:
            answer.append(1)
        else:
            answer.append(0)

    return '\n'.join(list(map(str, answer)))


print(solution(n, m, sorted(arr), numbers))
