from itertools import combinations
answer = []


def solution(array):
    n, *numbers = array
    result = list(combinations(numbers, 6))
    for i in range(len(result)):
        answer.append(' '.join(list(map(str, result[i]))))
    answer.append('')


while True:
    array = list(map(int, input().split()))
    if len(array) == 1:
        break
    solution(array)
for i in range(len(answer)-1):
    print(answer[i])
