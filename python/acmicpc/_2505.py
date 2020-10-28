from itertools import permutations
n = int(input())
numbers = list(map(int, input().split()))


def isValid(n, arr):
    for i in range(n):
        if arr[i] != i+1:
            return False
    return True


def answer(arr):
    if not arr:
        return '1 1' + '\n' + '1 1'
    if len(arr) == 1:
        return ' '.join(list(map(str, arr[0]))) + '\n' + '1 1'
    return ' '.join(list(map(str, arr[0]))) + '\n' + ' '.join(list(map(str, arr[1])))


def solution(n, numbers):
    # 그대로 나가는 경우
    temp = numbers.copy()
    if isValid(n, temp):
        return answer([])
    # 한번 뒤집어서 되는 경우
    history = []
    for i in range(n):
        if temp[i] != i+1:
            start = i
            end = temp.index(i+1)+1
            temp[start:end] = list(reversed(temp[start:end]))
            history.append([start+1, end])
            break
    if isValid(n, temp):
        return answer(history)
    # 두번 뒤집어서 되는 경우
    for i in range(n):
        if temp[i] != i+1:
            start = i
            end = temp.index(i+1)+1
            temp[start:end] = list(reversed(temp[start:end]))
            history.append([start+1, end])
            break
    if isValid(n, temp):
        return answer(history)
    # 리버스한다.
    history = []

    for i in range(n-1, -1, -1):
        if numbers[i] != i+1:
            end = i+1
            start = numbers.index(i+1)
            numbers[start:end] = list(reversed(numbers[start:end]))
            history.append([start+1, end])
            break
    if isValid(n, numbers):
        return answer(history)

    for i in range(n-1, -1, -1):
        if numbers[i] != i+1:
            end = i+1
            start = numbers.index(i+1)
            numbers[start:end] = list(reversed(numbers[start:end]))
            history.append([start+1, end])
            break

    if isValid(n, numbers):
        return answer(history)


#t = list(map(list, permutations([1, 2, 3, 4, 5], 5)))
# for numbers in t:
#     print(numbers)
print(solution(n, numbers))
