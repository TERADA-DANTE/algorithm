clients = 0
answer = 0
for _ in range(4):
    outBoard, onBoard = list(map(int, input().split()))
    clients -= outBoard
    clients += onBoard
    answer = max(answer, clients)
print(answer)
