n = int(input())

print(*['X' if '3' in str(i) or '6' in str(i) or '9' in str(i) else str(i)
        for i in range(1, n+1)])
