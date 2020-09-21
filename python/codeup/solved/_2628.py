a, b = sorted(list(map(int, input().split())))
c, d = sorted(list(map(int, input().split())))
[a, b, c, d] = [a, b, c, d] if a < c else [c, d, a, b]
if a < c < b:
    if d > b or d < a:
        print('cross')
    else:
        print('not cross')
else:
    if d > b and d < a:
        print('cross')
    else:
        print('not cross')
