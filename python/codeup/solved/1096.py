board = [[0]*19 for _ in range(19)]
n = int(input())
for _ in range(n):
    a, b = list(map(int, input().split()))
    board[a-1][b-1] = 1
answer = []
for b in board:
    answer.append(' '.join(list(map(str, b))))
print('\n'.join(answer))
