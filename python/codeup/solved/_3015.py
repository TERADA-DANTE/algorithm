n, m = list(map(int, input().split()))

scores = [input().split() for _ in range(n)]

print('\n'.join([name for name, score in sorted(
    scores, key=lambda v: -int(v[1]))[0:m]]))
