def solution(n, i=1):
    if n >= i:
        print('*'*i)
        solution(n, i+1)
    else:
        return


solution(int(input()))
