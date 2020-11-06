words = [list(input()) for _ in range(5)]


def solution(words):
    board = [[''] * 15 for _ in range(5)]
    for i in range(5):
        l = len(words[i])
        for j in range(l):
            board[i][j] = words[i][j]
    answer = [[''] * 5 for _ in range(15)]
    for i in range(15):
        for j in range(5):
            answer[i][j] = board[j][i]
    ret = ''
    for i in range(15):
        sentence = ''.join(answer[i])
        ret += sentence
    return ret


print(solution(words))
