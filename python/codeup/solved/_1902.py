
def solution(i):
    if i:
        print(i)
        solution(i-1)


solution(int(input()))
