import sys 
x, y ,w, h = map(int,sys.stdin.readline().split())
if x > w - x:
    xDistance = w - x 
else: 
    xDistance = x 
if y > h - y:
    yDistance = h - y
else: 
    yDistance = y 
     
print(min(xDistance,yDistance))