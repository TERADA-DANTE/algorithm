n = int(input())
arr = list(map(int, input().split()))
b, c = list(map(int, input().split()))
cnt = n
newArr = [0 if v < b else v-b for v in arr]

for v in newArr:
    if v:
        cnt += int((v-1) // c)+1
print(cnt)
# 0이면 안들어가도됨
#  12 3 .... c 까지는 1명 들어가야됨.
