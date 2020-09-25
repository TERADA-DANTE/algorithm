n = int(input())
preferences = [[0, 0, 0, 0] for _ in range(3)]
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    preferences[0][0] += a
    preferences[0][a] += 1
    preferences[1][0] += b
    preferences[1][b] += 1
    preferences[2][0] += c
    preferences[2][c] += 1
preferences = sorted(enumerate(preferences, start=1),
                     key=lambda v: (-v[1][0], -v[1][3], -v[1][2]))
if preferences[0][1][3] == preferences[1][1][3] and preferences[0][1][2] == preferences[1][1][2]:
    print(0, preferences[0][1][0])
else:
    print(preferences[0][0], preferences[0][1][0])
