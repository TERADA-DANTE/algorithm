n = int(input())

scores = [list(map(int, input().split()))
          for _ in range(n)]
scores.sort(key=lambda v: -v[2])
print(scores[0][0], scores[0][1])
print(scores[1][0], scores[1][1])
if scores[0][0] == scores[1][0] == scores[2][0]:
    i = 2
    while scores[i][0] == scores[i-1][0]:
        i += 1
    print(scores[i][0], scores[i][1])
else:
    print(scores[2][0], scores[2][1])
