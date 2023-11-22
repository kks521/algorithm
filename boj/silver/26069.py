#26069 실버4 스택 

import sys 

cnt = int(sys.stdin.readline())
dance = ['ChongChong']
for _ in range(cnt):
    temp = sys.stdin.readline().split()
    if temp[0] in dance or temp[1] in dance:
        dance.extend(temp)

print(len(set(dance)))