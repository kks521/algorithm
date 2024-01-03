#2630, 실버2, 분할정복
import sys 

n = int(sys.stdin.readline())
arr = []
blue = 0 
white = 0
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def solve(x,y,n):
    global white, blue
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                solve(x,y,n//2)
                solve(x,y+n//2,n//2)
                solve(x+n//2,y,n//2)
                solve(x+n//2,y+n//2,n//2)
                return
    if color == 0: 
        white += 1
    else: 
        blue += 1 

solve(0,0,n)

print(white)
print(blue)