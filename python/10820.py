while True:
    try:
        [letters, counter] = [input(), [0]*4]
        for letter in letters:
            if letter.isupper():
                counter[1] += 1
            elif letter == ' ':
                counter[3] += 1
            elif letter.isdigit():
                counter[2] += 1
            else:
                counter[0] += 1
        print('\n'.join(map(str, counter)))
    except EOFError:
        break
