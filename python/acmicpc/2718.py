answer = []
def solution(n):


for _ in range(int(input())):
    n = int(input())
    answer.append(solution(n))
print('\n'.join(list(map(str, answer))))
