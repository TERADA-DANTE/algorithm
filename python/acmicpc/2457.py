from collections import deque
n = int(input())
flowers = [list(map(int, input().split())) for _ in range(n)]
# 4, 6, 9, 11월은 30일까지 있고,
# 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며,
# 2월은 28일까지만 있다.
# 1월 1일 ~ 12월 31일
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = [None] * (1+31*7+28+30*4)
# n월 n일은 n-1월까지 월 수 다 더하고,
# n월 n일 == months[0:n]+m
answer = []


def d(month, day): return sum(months[0:month])+day


def solution(n, flowers):
    global answer

    flowers.sort(key=lambda v: (v[0], v[1], v[2], v[3]))
    queue = deque(flowers)
    while queue:
        print(answer)
        sM, sD, eM, eD = queue.popleft()
        start, end = d(sM, sD), d(eM, eD)
        if not answer:
            answer.append([start, end])
            break
        left, right = answer[-1][0], answer[-1][1]
        if left == start and right < end:
            answer.pop()
            answer.append([start, end])
        elif left < start <= right:

            # 빈경우 그냥 넣는다
            # 그 외의 경우
            # 	스타트가 왼쪽에 겹치는경우
            # 		엔드가 오른쪽보다 작은경우 => 무시
            # 		엔드가 오른쪽에 겹치는경우 => 무시
            # 		엔드가 오른쪽보다 큰 경우 => 앞에꺼 팝. 스타트엔드 들억마
            # 	스타트가 왼쪽과 오른쪽 사이에 있는 경우
            # 		엔드가 오른쪽보다 작은경우 => 무시
            # 		엔드가 오른쪽에 겹치는경우 => 무시
            # 		엔드가 오른쪽보다 큰 경우 =>
            # 			스타트가 d(3,1)보다 작거나 같으면 다 팝하고 어펜드
            # 			스타트가 d(3,1)보다 크다면 그냥 어펜드
            # 	스타트가 오른쪽을 넘어가는 경우 => 0반환
print(solution(n, flowers))
