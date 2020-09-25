import re
n = int(input())


class Stack:
    def __init__(self):
        self._arr = []

    def push(self, data):
        self._arr.append(data)
        return

    def top(self):
        if self._arr:
            return self._arr[-1]
        return -1

    def pop(self):
        if self._arr:
            self._arr.pop()
            return
        return

    def size(self):
        return len(self._arr)

    def empty(self):
        return 'false' if len(self._arr) else 'true'


stack = Stack()
for _ in range(n):
    commands = re.findall(r'[a-z]+|\d+', input())
    if commands[0] == 'push':
        stack.push(commands[1])
    elif commands[0] == 'top':
        print(stack.top())
    elif commands[0] == 'pop':
        stack.pop()
    elif commands[0] == 'size':
        print(stack.size())
    else:
        print(stack.empty())
