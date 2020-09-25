n = int(input())
papers = list(map(int, input().split()) for _ in range(n))
board = [[0]*100 for _ in range(100)]


def fill(x, y):
    for i in range(10):
        for j in range(10):
            board[x+i][y+j] = 1


for paper in papers:
    x, y = paper
    fill(x, y)
cnt = 0
for b in board:
    cnt += sum(b)
print(cnt)
