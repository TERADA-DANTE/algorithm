n = int(input())
for _ in range(n):
    A, *a = list(map(int, input().split()))
    B, *b = list(map(int, input().split()))
    i = 4
    while i:
        if a.count(i) != b.count(i):
            if a.count(i) > b.count(i):
                print('A')
            else:
                print('B')
            break
        i -= 1
    if not i:
        print('D')
