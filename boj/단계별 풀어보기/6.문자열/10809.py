import sys 
word = sys.stdin.readline().strip()
for i in range(97,123):
    i = chr(i)
    if i not in word:
        print(-1,end=' ')
    elif i in word: 
        print(word.find(i),end=' ')
