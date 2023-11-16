import sys 

n,m,block = map(int,sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = sys.maxsize
idx = 0 

for floor in range(257):
    exceed_block, lack_block = 0, 0

    for i in range(n):
        for j in range(m):

            if arr[i][j] > floor :
                exceed_block += arr[i][j] - floor
            else : 
                lack_block += floor - arr[i][j]

    if exceed_block + block >= lack_block :
        if (exceed_block * 2) + lack_block <= ans:
            ans = (exceed_block * 2) + lack_block
            idx = floor


print(ans, idx)

