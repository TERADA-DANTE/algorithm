numbers = list(map(int, input().split()))
evens = [i for i in numbers if not i % 2]
odds = [i for i in numbers if i % 2]

if not evens:
    print(max(odds))
elif not odds:
    print(max(evens))
else:
    print(max(odds) + max(evens))
