import sys 
n = int(sys.stdin.readline())
lst = list()
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))

for h1,w1 in lst:
    cnt = 1 

    for h2, w2 in lst:
        if h1 < h2 and w1 < w2: 
            cnt += 1
    print(cnt,end=' ')  
 