import sys
n = int(sys.stdin.readline())
words = []
for i in range(n):
    words.append(sys.stdin.readline().rstrip())
words = list(set(words))
words.sort(key=lambda x:(len(x),x))

for j in words:
    print(j)