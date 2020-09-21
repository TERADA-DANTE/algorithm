n = int(input())
dp = [[1, [(0, 0)]], [2, [(0, 0)]], [4, [(1, 0)]]]
for i in range(n-3):
    one = dp[-1][1]
    two = dp[-2][1]
    three = dp[-3][1]
