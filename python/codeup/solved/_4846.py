n = int(input())
tuples = [list(map(int, input().split())) for _ in range(n)]


def allocation(student, apple):
    return apple % student


remainants = [allocation(*tuple) for tuple in tuples]
print(sum(remainants))
