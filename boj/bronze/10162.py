#10162, 브론즈3, 그리디 알고리즘
import sys 
time = int(sys.stdin.readline())
ans = []
    
ans.append(str(time // 300))
time %= 300 
    
ans.append(str(time // 60))
time %= 60
    
ans.append(str(time // 10))

if time % 10: 
    print(-1)
else:
    print(' '.join(ans))

