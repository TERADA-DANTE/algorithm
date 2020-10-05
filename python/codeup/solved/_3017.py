n = int(input())
students = [list(map(int, input().split())) for _ in range(n)]
students = list(enumerate(students, start=1))
students.sort(key=lambda v: (-v[1][0], -v[1][1], v[0]))
for i in range(n):
    a, [b, c] = students[i]
    print(a, b, c)
