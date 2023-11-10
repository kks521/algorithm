import sys

def round2(num):
        return int(num) + (1 if num-int(num) >= 0.5 else 0)

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
cutNum = round2(len(arr) * 0.15)
arr.sort()
if n == 0:
    score = 0 
else:
    for j in range(cutNum):
        arr[j] = 0
        arr[-(j+1)] = 0 
    score = round2(sum(arr) / (len(arr)- 2*cutNum))
print(score)