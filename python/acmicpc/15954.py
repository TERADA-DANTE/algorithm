# 문제 이해 불가
import math
n, k = list(map(int, input().split()))
numbers = list(map(int, input().split()))
answer = float('inf')
for i in range(n-k):
    avrg = float(sum(numbers[i:i+k])/k)
    deviation = math.sqrt(
        float(sum([(numbers[i+j]-avrg) ** 2 for j in range(k)])/k))
    answer = min(answer, deviation)
print(answer)
