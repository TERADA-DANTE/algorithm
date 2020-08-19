import sys
initials = list(sys.stdin.readline()[0:-1])
n = int(sys.stdin.readline())


class Node():
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList():
    def __init__(self, initials=[]):
        self.head = Node(None, None, None)
        for initial in initials:
            self.append(initial)

    def append(self, data):
        self.head.next = Node(data, self.head, Node(None, None, None))
        self.head = self.head.next
        self.head.next.prev = self.head

    def L(self):
        if self.head.prev:
            self.head = self.head.prev

    def D(self):
        if self.head.next.data:
            self.head = self.head.next

    def B(self):
        if self.head.prev:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.prev

    def P(self, data):
        self.head.next = Node(data, self.head, self.head.next)
        self.head = self.head.next
        self.head.next.prev = self.head

    def getStr(self):
        while self.head.prev:
            self.head = self.head.prev
        self.head = self.head.next
        s = ''
        while self.head.data:
            s += self.head.data
            self.head = self.head.next
        return s


def solution(n):
    link = LinkedList(initials)
    for _ in range(n):
        command = sys.stdin.readline().split()
        if len(command) == 2:
            link.P(command[1])
        else:
            if command[0] == 'L':
                link.L()
            elif command[0] == 'D':
                link.D()
            else:
                link.B()
    return link.getStr()


print(solution(n))
