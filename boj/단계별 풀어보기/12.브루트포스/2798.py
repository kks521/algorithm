import sys 
count, target = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
result = 0 
for i in range(count):
    for j in range(i+1,count):
        for k in range(j+1,count):
            if cards[i] + cards[j] +cards[k] <= target and cards[i] + cards[j] +cards[k] > result:
                result = cards[i] + cards[j] +cards[k]



print(result)

