#1946, 실버1, 그리디 알고리즘, 정렬
import sys 
def getScore(n):
    ranks = list()
    for i in range(n):
        ranks.append(list(map(int,sys.stdin.readline().split())))
    return ranks
def checkScore(n):
    cnt=0
    ranks = getScore(n)
    ranks.sort(key=lambda x: (-x[0],-x[1]))
    for i in range(n):
        check = ranks[i]
        checkIndex = ranks.index(check)
        for s1,s2 in reversed(ranks[checkIndex:]):
            if s1 < check[0] and s2 < check[1]:
                cnt += 1
                break

    return n - cnt 
case = int(sys.stdin.readline())

for i in range(case):
    n = int(sys.stdin.readline())
    print(checkScore(n))
