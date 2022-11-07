import sys 
n = int(sys.stdin.readline())

print(stars*3)

def star(k):
    cnt = 1
    for i in range(k): 
        if cnt == 2:
            print('***\n* *\n***'*(k-1))
        else:
            print('stars'*k,end='')
        cnt += 1
def solve(n):
    star(n//3) 
def make(l):
    print('***'*l)
    print('* *'*l)
    print('***'*l)

solve(n)