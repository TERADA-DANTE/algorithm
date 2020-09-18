h, b, c, s = list(map(int, input().split()))

print('%.1f' % float((h*b*c*s)/(1024*8*1024)), 'MB')
