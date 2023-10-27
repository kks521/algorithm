import sys 
angle = []
angle.append(int(sys.stdin.readline()))
angle.append(int(sys.stdin.readline()))
angle.append(int(sys.stdin.readline()))
if sum(angle) != 180:
    print('Error')
else:
    if len(set(angle)) == 1:
        print('Equilateral')
    elif len(set(angle)) == 2:
        print('Isosceles')
    else:
        print('Scalene')