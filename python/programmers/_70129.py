def solution(s, cnt=0, history=0):
    if s == '1':
        return [cnt, history]
    h = len(s)-s.count('1')
    return solution(str(bin(s.count('1')))[2:], cnt+1, history+h)


print(solution('0111010'))
