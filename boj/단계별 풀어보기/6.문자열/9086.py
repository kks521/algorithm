import  sys

cnt = int(sys.stdin.readline())
for i in range(cnt):
    word = sys.stdin.readline().strip()
    print(f'{word[0]}{word[-1]}')