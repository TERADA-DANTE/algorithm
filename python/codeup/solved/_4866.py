import math
n, k = list(map(int, input().split()))
students = sorted([list(map(int, input().split()))
                   for _ in range(n)], key=lambda v: v[1])
filtered = [[0, 0], [0, 0], [0, 0]]
while students:
    sex, grade = students.pop()
    filtered[int((grade-1)//2)][sex] += 1

a = math.ceil(sum(filtered[0])/k)
b = math.ceil(filtered[1][0]/k) + math.ceil(filtered[1][1]/k)
c = math.ceil(filtered[2][0]/k) + math.ceil(filtered[2][1]/k)
print(a+b+c)
