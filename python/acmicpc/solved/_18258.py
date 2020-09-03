from collections import deque
import sys
input = sys.stdin.readline


class Queue:
    def __init__(self):
        self.array = deque([])

    def push(self, data):
        self.array.append(data)

    def pop(self):
        return self.array.popleft() if self.array else -1

    def size(self):
        return len(self.array)

    def empty(self):
        return 0 if self.array else 1

    def front(self):
        return self.array[0] if self.array else -1

    def back(self):
        return self.array[-1] if self.array else -1


queue = Queue()
answer = []
for _ in range(int(input())):
    result = None
    command = input().split()
    if len(command) == 2:
        queue.push(command[1])
    elif command[0] == 'pop':
        result = queue.pop()
    elif command[0] == 'size':
        result = queue.size()
    elif command[0] == 'empty':
        result = queue.empty()
    elif command[0] == 'front':
        result = queue.front()
    elif command[0] == 'back':
        result = queue.back()
    if result is not None:
        answer.append(result)
print('\n'.join(list(map(str, answer))))
