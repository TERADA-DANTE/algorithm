n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
print(sum(list(map(lambda v: v[0]*v[1], zip(a, b)))))
