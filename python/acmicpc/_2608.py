strings = [input() for _ in range(2)]
# 보통 큰 숫자를 왼쪽에 작은 숫자를 오른쪽에 쓴다
# V, L, D는 한 번만 사용할 수 있다.
# I, X, C, M은 연속해서 세 번까지만 사용할 수 있다
# 작은 숫자가 큰 숫자의 왼쪽에 오는 경우는 다음과 같다.
# IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
# 이들 각각은 한 번씩만 사용할 수 있다.
# IV 와 IX 는 같이 쓸 수 없다.
# XL 과 XC 는 같이 쓸 수 없다.
# CD 와 CM 는 같이 쓸 수 없다.
# 모든 수는 가능한 가장 적은 개수의 로마 숫자들로 표현해야 한다.
# 자리 수로
romans = [['I', 1, 0], ['IV', 4, 1], ['V', 5, 0], ['IX', 9, 1], ['X', 10, 0], ['XL', 40, 2], [
    'L', 50, 0], ['XC', 90, 2], ['C', 100, 0], ['CD', 400, 3], ['D', 500, 0], ['CM', 900, 3], ["M", 1000, 0]]
r = dict()
for letter, number, _ in romans:
    r[letter] = number


def toNumber(string):
    result = 0
    for v in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
        if v in string:
            string = string.replace(v, '')
            result += r[v[1]] - r[v[0]]
    for s in string:
        result += r[s]
    return result


def toString(number):
    result = []
    while number:

        for i in range(len(romans)-1, -1, -1):
            letter, n, flag = romans[i]
            if n <= number:
                result.append([letter] * int(number//n))
                if flag:
                    for j in range(len(romans)-1, -1, -1):
                        _, _, f = romans[j]
                        if f == flag:
                            romans.pop(j)
                number = number % n
                break
    return result


def solution(strings):
    ret = sum([toNumber(string) for string in strings])
    result = toString(ret)
    return str(ret) + '\n'+''.join(list(map(lambda v: ''.join(v), result)))


print(solution(strings))
