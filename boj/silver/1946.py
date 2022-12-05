#1946, 실버1, 그리디 알고리즘, 정렬
import sys 
def getScore(n):
    ranks = list()
    for i in range(n):
        ranks.append(list(map(int,sys.stdin.readline().split())))
    return ranks
def checkScore(n):
    cnt = 1
    ranks = getScore(n)
    ranks.sort(key=lambda x: x[0])
    standard = ranks[0][1]
    for i in range(1,n):
        check = ranks[i][1]
        if check < standard:
            standard = check
            cnt += 1
    return cnt 
case = int(sys.stdin.readline())

for i in range(case):
    n = int(sys.stdin.readline())
    print(checkScore(n))
