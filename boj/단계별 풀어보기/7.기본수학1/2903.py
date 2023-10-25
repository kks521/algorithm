import sys 
n = int(sys.stdin.readline())
dot = 2 
answer = [ ]
for i in range(15):
    dot = 2 * dot - 1 
    answer.append(dot**2)
print(answer[n-1])