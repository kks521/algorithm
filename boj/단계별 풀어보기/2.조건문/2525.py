import sys
hour, min = map(int,sys.stdin.readline().split())
time =int(sys.stdin.readline())
min = min + time
if min >= 60: 
    hour += min // 60
    min -= 60 * (min // 60)  
    if hour >= 24: 
        hour = hour -24 
print(hour,min)        
