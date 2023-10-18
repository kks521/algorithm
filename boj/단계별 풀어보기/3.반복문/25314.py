import sys 
answer = ''
n = int(sys.stdin.readline())
for i in range(n//4):
    answer += 'long '
answer +=  'int'
print(answer)