import sys
initials = list(sys.stdin.readline()[0:-1])
n = int(sys.stdin.readline())


class Node():
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class LinkedList():
    def __init__(self):
        self.body = Node()

    def append(self, data):
        self.body.next = Node(data, self.body, Node())
        self.body = self.body.next

    def L(self):
        if self.body.prev:
            self.body = self.body.prev

    def D(self):
        if self.body.next:
            self.body = self.body.next

    def B(self):
        if self.body.prev:
            self.body.next.prev = self.body.prev
            self.body.prev.next = self.body.next

    def P(self, data):
        self.body.next.prev = Node(data, self.body, self.body.next)
        self.body.next = Node(data, self.body, self.body.next)
        self.body = self.body.next

    def show(self):
        while self.body.prev:
            self.L()
        self.D()
        while self.body.data:
            print(self.body.data)
            self.D()


def solution(n):
    # Initializing
    link = LinkedList()
    for i in range(len(initials)):
        link.append(initials[i])
    # for i in range(n):
    #     command = sys.stdin.readline().split()
    #     if len(command) == 2:
    #         link.P(command[1])


print(solution(n))
