import sys
import math 
day, night, goal = map(int,sys.stdin.readline().split())
result = math.ceil((goal - day) / (day - night)) + 1
print(result)