#1012, 실버2, 그래프
import sys 
from collections import deque

cnt = int(sys.stdin.readline())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a,b):
    queue = deque([(a,b)])
    graph[a][b] = 0

    while queue: 
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= width or ny < 0 or ny >= height: 
                continue 
            if graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0 
    return
            

for __ in range(cnt):
    width, height, n = map(int,sys.stdin.readline().split())
    graph = [[0]* height for x in range(width)]
    ans = 0 

    for _ in range(n):
        x,y = map(int,sys.stdin.readline().split())
        graph[x][y] = 1

    for w in range(width):
        for h in range(height):
            if graph[w][h] == 1:
                bfs(w,h)
                ans += 1

    print(ans)


