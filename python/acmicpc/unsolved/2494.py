from collections import deque
n = int(input())
initial = input()
target = input()


def solution(n, initial, target):
    dp = {}
    queue = deque([[0, initial, []]])

    while queue:
        cnt, stringNumber, history = queue.popleft()

        if dp.get(stringNumber):
            continue
        dp[stringNumber] = cnt
        if stringNumber == target:
            answer = {}
            for i in range(len(history)):
                t = f'{history[i][0]} {history[i][1]}'
                if answer.get(t):
                    answer[t] += history[i][1]
                else:
                    answer[t] = history[i][1]
            ret = [f'{s[0]} {answer[s]}' for s in list(answer.keys())]
            return str(cnt)+'\n'+'\n'.join(ret)
        # 왼쪽으로
        for i in range(n):
            head = stringNumber[:i] if stringNumber else ['']
            tail = [str(int(number)+1)[-1] for number in stringNumber[i:]]
            newNumber = ''.join(head)+''.join(tail)

            queue.append([cnt+1, newNumber, history+[[i+1, 1]]])

        # 오른쪽으로
        for i in range(n):
            head = stringNumber[:i] if stringNumber else ['']
            body = str(10+int(stringNumber[i])-1)[-1]
            tail = stringNumber[i+1:]
            newNumber = ''.join(head)+body+''.join(tail)

            queue.append([cnt+1, newNumber, history+[[i+1, -1]]])


print(solution(n, initial, target))
