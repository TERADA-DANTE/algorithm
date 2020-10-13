from collections import deque


def solution(food_times, k):
    times = deque((enumerate(food_times, start=1)))
    while(k):
        index, time = times.popleft()
        if time:
            times.append((index, time-1))
            k -= 1
        else:
            times.append((index, time))
    return times[0][0]


print(solution([3, 1, 2], 5))
