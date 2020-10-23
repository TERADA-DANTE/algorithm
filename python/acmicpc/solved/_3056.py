from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())

agents = [list(map(lambda v: int(v)/100, input().split())) for _ in range(n)]


def solution(n, agents):
    dp = [0] * (2**n)
    for i in range(n):
        dp[1 << i] = agents[i][0]
    for cnt in range(1, n+1):
        for number in range(int('1'*cnt, 2), int('1'*cnt+'0'*(n-cnt), 2)+1):
            temp = number
            c = 0
            while temp:
                c += temp % 2
                temp = int(temp//2)
            if c == cnt:
                for shift in range(n):
                    bit = 1 << shift
                    if not number & bit:
                        dp[number | bit] = max(
                            dp[number | bit], (dp[number] if dp[number] else 1)*agents[shift][cnt])

    return dp[-1]*100


print((solution(n, agents)))
