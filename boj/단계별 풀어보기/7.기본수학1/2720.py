import sys 
cnt = int(sys.stdin.readline())
coin = [25,10,5,1]
for i in range(cnt):
    change = int(sys.stdin.readline())
    answer = []
    for c in coin: 
        print(change//c, end=' ')
        change %= c

    
