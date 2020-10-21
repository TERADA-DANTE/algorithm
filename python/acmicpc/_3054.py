arr = list(enumerate(input(), start=1))
# 각 단어에 대해서 웬디 | 피터팬 프레임을 작성한다.
# 이어 붙인다.


def frame(i, v):
    result = [['.']*5 for _ in range(5)]
    result[2][2] = v
    for j in range(5):
        k = j if j <= 2 else 4-j
        result[2+k][j] = '#' if i % 3 else '*'
        result[2-k][j] = '#' if i % 3 else '*'
    return result


frames = [frame(i, v) for i, v in arr]
while len(frames) > 1:
    last = frames.pop()
    pre = frames.pop()
    result = [None] * 5
    for i in range(5):
        result[i] = pre[i][:4]+last[i]
    frames.append(result)
for i in range(1, len(frames[0][0])):
    if frames[0][2][i] == '#' and frames[0][1][i-1] == '*':
        frames[0][2][i] = '*'
for i in range(5):
    print(''.join(frames[0][i]))
