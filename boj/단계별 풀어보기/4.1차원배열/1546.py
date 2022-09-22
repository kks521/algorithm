import sys 
cnt = int(sys.stdin.readline())
score = list(map(int,sys.stdin.readline().split()))
top_score = max(score)
total_score = 0
for i in score:
    total_score += i / top_score * 100 
print(total_score/cnt)
