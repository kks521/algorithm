import sys 
cnt = int(sys.stdin.readline())

while True:
    if cnt == 0:
        break
    score= 0
    total = 0  
    ox = sys.stdin.readline().strip()
    for i in ox: 
        if i == 'O':
            score += 1 
            total += score 
        elif i == 'X':
            score = 0 
    print(total)  
     
    cnt -= 1 
