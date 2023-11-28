#9372, 실버4 트리 
import sys 
cnt = int(sys.stdin.readline())

for _ in range(cnt):
    a, b = map(int,sys.stdin.readline().split())
    for _ in range(b):
       sys.stdin.readline()
    print(a-1)