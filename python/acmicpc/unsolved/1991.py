n = int(input())


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = None if left == '.' else left
        self.right = None if right == '.' else right


def preOrder(tree, root, answer=''):
    answer += root.data
    if root.left:
        answer += preOrder(tree, tree[root.left])
    if root.right:
        answer += preOrder(tree, tree[root.right])
    return answer


def solution(n):
    [tree, answer] = [dict(), []]
    for _ in range(n):
        data = input().split()
        tree[data[0]] = Node(data[0], data[1], data[2])
    answer += [preOrder(tree, tree['A'])]
    return '\n'.join(answer)


print(solution(n))
