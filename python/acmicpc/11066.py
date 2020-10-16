def solution(n, numbers):
    4 3 3 5
    7 + 8 + 15 = 30
    7 6 8
    7: 7 3 5
    6: 4 6 5
    8: 4 3 8
    a+b + a+b+c + a+b+c+d


for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    print(solution(n, numbers))
