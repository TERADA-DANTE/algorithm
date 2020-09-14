def solution(a):
    l = len(a)
    cols = [len([a[i][j] for i in range(l) if a[i][j]])
            for j in range(len(a[0]))]
    return cols
    # 모든 수가 0 또는 1로 이루어진 2차원 배열 a가 주어집니다.
    # 다음 조건을 모두 만족하는 2차원 배열 b의 경우의 수를
    # (10^7 + 19)로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

    # b의 모든 원소는 0 아니면 1입니다.
    # a와 b의 크기가 같습니다.
    # a의 i번째 열과 b의 i번째 열에 들어 있는 1의 개수가 같습니다.
    #
    # b의 각 행에 들어 있는 1의 개수가 짝수입니다. (0도 짝수입니다.)
    # 제한 사항
    # a의 행의 개수는 1 이상 300 이하입니다.
    # a의 각 행의 길이는 1 이상 300 이하로 모두 동일합니다.
    # 꽉차있거나 비어있는 열은 고정 => 개수 각각
    # 꽉차있는 것의 개수 => 고정 + 홀수이면 영향주고 짝수이면 영향 안줌.
    # 비어있는 열의 개수 => 고정 + 개수가 영향 안주므로 그냥 뺌
    # 열의 순서는 상관없다. (행?)
    2  1  0  1  2


print(solution([[1, 0, 0, 1, 1], 3 0 2 0 0 2 2 0
                [0, 0, 0, 0, 0], 0 0 0 2 0 2 0 2
                [1, 1, 0, 0, 0], 2 0 0 0 2 0 2 2
                [0, 0, 0, 0, 1]  1 6 4 4 4 2 2 2
                # 합 => 6　　　　　　　. . . . . 　　　　　　　
                ])
      )
# 1을 싹다 위로 올려서 행중에 1의 개수가 홀수가 하나라도 있다면 못만든다.
[1, 1]
[0, 1]
[1, 0]
[0, 0]
2  1  0  1  2
[1, 1, 0, 1, 1] 4
[1, 0, 0, 0, 1] 2
[0, 0, 0, 0, 0] 0
[0, 0, 0, 0, 0] 0

2  4  2
[1, 1, 1] 3
[1, 1, 1] 3
[0, 1, 0] 1
[0, 1, 0] 1

2  0  0
[1, 0, 0] 1
[1, 0, 0] 1

1  2  1
[1, 1, 1] 1
[0, 1, 0] 1
