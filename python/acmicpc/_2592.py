from collections import Counter

numbers = [int(input()) for _ in range(10)]
average = int(sum(numbers)/10)
common = Counter(numbers).most_common(1)

print(str(average) + '\n'+str(common[0][0]))
