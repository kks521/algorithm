import sys
case = int(sys.stdin.readline())
for i in range(case):
    num, word = sys.stdin.readline().split()
    cnt = 0
    for j in word:
        if cnt ==len(word)-1:
            print(j*int(num))
        else:
            print(j*int(num),end='')
            cnt += 1 
