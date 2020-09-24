s = input()
years = s[0:2]
months = s[2:4]
days = s[4:6]
security = int(s[7])
print(('20' if security > 2 else '19')+str(years)+'/' +
      str(months)+'/'+str(days), 'M' if security % 2 else 'F')
