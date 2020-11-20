n = int(input())
tree = dict()
preO = []
inO = []
postO = []
for _ in range(n):
    root, left, right = input().split()
    tree[root] = dict()
    tree[root]['left'] = left
    tree[root]['right'] = right


def preOrder(root):
    global preO
    preO.append(root)
    if tree[root]['left'] != '.':
        preOrder(tree[root]['left'])
    if tree[root]['right'] != '.':
        preOrder(tree[root]['right'])


def inOrder(root):
    global inO
    if tree[root]['left'] != '.':
        inOrder(tree[root]['left'])
    inO.append(root)
    if tree[root]['right'] != '.':
        inOrder(tree[root]['right'])


def postOrder(root):
    global postO
    if tree[root]['left'] != '.':
        postOrder(tree[root]['left'])
    if tree[root]['right'] != '.':
        postOrder(tree[root]['right'])
    postO.append(root)


preOrder('A')
inOrder('A')
postOrder('A')
print('\n'.join(list(map(lambda v: ''.join(v), [preO, inO, postO]))))
