numbers = list(map(int, input().split()))
print(sum(list(map(lambda v: v**2, numbers))) % 10)
