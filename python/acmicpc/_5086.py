while True:
    a, b = list(map(int, input().split()))
    if not a and not b:
        break
    if not b % a:
        print('factor')
    elif not a % b:
        print('multiple')
    else:
        print('neither')
