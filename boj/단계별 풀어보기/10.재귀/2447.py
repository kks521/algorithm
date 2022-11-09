import sys 
n = int(sys.stdin.readline())

def make(l):
    if l == 3:
        return['***','* *','***']
    
    star = make(l//3)
    stars = []
    for i in star:
        stars.append(i * 3)
    for i in star:
        stars.append(i + ' '*(l//3)+i)
    for i in star:
        stars.append(i*3)     
    return stars
t = make(n)
print('\n'.join(make(n)))