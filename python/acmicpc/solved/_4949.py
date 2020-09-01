import re


def isPair(string):
    if string == '':
        return True
    if re.search(r'\[\]|\(\)', string):
        return isPair(re.sub(r'\[\]|\(\)', '', string))
    return False


answer = []
while True:
    string = input()
    if string == '.':
        break
    string = re.sub(r'\w| |\.', '', string)
    answer.append('yes' if isPair(string) else 'no')
print('\n'.join(answer))
