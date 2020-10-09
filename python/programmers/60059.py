from collections import deque

# 어렵다...


def rorate(arr):
    return list(map(list, zip(*arr[::-1])))


def availableKey(key, lock):


def solution(key, lock):
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    l = len(key)
    for _ in range(1):
        isVisited = [[None] * (2*len(key)+1) for _ in range(2*len(key)+1)]
        isVisited[l][l] = True
        queue = deque([[key, 5, 5]])
        while queue:
            q, row, col = queue.popleft()
            # 키가 맞는지 확인해야됨
            if availableKey(q, lock):
                return True
            for r, c of moves:
                if 0 <= row+r < l and 0 <= col+c < l and not isVisited[row+r][col+c]:
                    # 오른쪽
                    # 왼쪽
                    # 위쪽
                    # 아래쪽
        key = rorate(key)

    # 4각도에 대해서 테스트한다.
    # 각 각도에 대해서 좌상 상 우상 우 우하 하 좌하 좌 9가지 이동 패턴을 구성한다.
    # 전체 탐색한다.
    # 너무 복잡도가 상승한다.
    # BFS? 방문 설정해서 중복 줄이고.
    # 클래스 설정한다.
    # 초기 키값으로 이니셜라이징 한다.
    # 로테이트 함수 생성 => 90도 회전
    # move 함수 생성 => 모든 경우의 수 생성하여 배열로 반환
    # 배열에서 정답찾으면 트루 폴스 반환
print(solution(	[[0, 0, 0], [1, 0, 0], [0, 1, 1]],
                [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
