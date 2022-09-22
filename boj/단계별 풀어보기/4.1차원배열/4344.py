import sys 
cnt = int(sys.stdin.readline())

for i in range(cnt):
    total = 0 
    scores = list(map(int,sys.stdin.readline().split()))
    average = sum(scores[1:])/scores[0]
    for score in scores[1:]:
        if score > average:
            total += 1
    result = total/scores[0]*100
    print(f'{result:.3f}%')