#1003, silver3, dp
import sys 

zero = [1,0,1]
one = [0,1,1]

cnt = int(sys.stdin.readline())
for i in range(cnt):
    num = int(sys.stdin.readline())
    if num >= len(zero):
        while num >= len(zero):
            zero.append(zero[-1]+zero[-2])
            one.append(one[-1]+one[-2])
        print(zero[-1],one[-1])
    else: 
        print(zero[num],one[num])