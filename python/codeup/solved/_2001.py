pastas = [int(input()) for _ in range(3)]
juices = [int(input()) for _ in range(2)]
print('%.1f' % float((min(pastas) + min(juices)) * 1.1))
