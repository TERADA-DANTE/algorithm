from itertools import combinations, permutations
n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def getScore(players):
    enemies = [i for i in range(1, n+1) if i not in players]
    return abs(sum([board[p1-1][p2-1]+board[p2-1][p1-1] for p1, p2 in combinations(players, 2)]) -
               sum([board[q1-1][q2-1]+board[q2-1][q1-1] for q1, q2 in combinations(enemies, 2)]))


def solution(n, board):
    return min([getScore(players) for players in list(combinations(range(1, n+1), n//2))])


print(solution(n, board))
