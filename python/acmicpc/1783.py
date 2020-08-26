n, m = list(map(int, input().split()))


def solution(n, m, cnt=1):
    [row, col] = [0, 0]
    if row == 1 or col == 1 or row == 2 and col == 2:
        return 1
    # 가로 7부터는
    while True:
        print(row, col, cnt)
        # 1번 할 수 있는지
        if row+2 < n and col+1 < m:
            row += 2
            col += 1
    # 4번 할 수 있는지
        elif 0 <= row-2 and col+1 < m:
            row -= 2
            col += 1
    # 2번 할 수 있는지
        elif row+1 < n and col+2 < m:
            row += 1
            col += 2
    # 3번 할 수 있는지
        elif 0 <= row-1 and col+2 < m:
            row -= 1
            col += 2
        else:
            break
        cnt += 1
    return cnt


print(solution(n, m))
