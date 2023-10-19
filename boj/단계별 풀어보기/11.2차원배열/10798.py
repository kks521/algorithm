import sys 
answer = ''
s = [""]*20

for i in range(5):
    word = sys.stdin.readline().strip()

    for j in range(len(word)):
        s[j] +=  word[j]

for k in s:
    answer += k
    
print(answer)