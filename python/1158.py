import time

n, k = list(map(int, input().split()))


class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Link():
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            self.head.next = Node(data, self.head)
            self.head = self.head.next

    def coronize(self, data):
        self.head.next = Node(data, self.head)
        self.head = self.head.next
        next = self.head.next
        while self.head.prev:
            self.head = self.head.prev
        self.head.prev = next


def solution(n, k):
    t = k


s = time.time()
print(solution(n, k))
print(time.time()-s)
