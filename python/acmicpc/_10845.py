from collections import deque
import sys
input = sys.stdin.readline
answer = []
n = int(input())
queue = deque()

for _ in range(n):
    commands = input().split()
    if commands[0] == 'push':
        queue.append(commands[1])
    elif commands[0] == 'pop':
        if queue:
            answer.append(queue.popleft())
        else:
            answer.append(-1)
    elif commands[0] == 'size':
        answer.append(len(queue))
    elif commands[0] == 'empty':
        answer.append(1 if not queue else 0)
    elif commands[0] == 'front':
        answer.append(queue[0])
    else:
        answer.append(queue[-1])
print('\n'.join(list(map(str, answer))))
