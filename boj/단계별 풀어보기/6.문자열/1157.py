import sys
word = input().upper()
word_set = list(set(word))
check  = []
for i in word_set:
    cnt = word.count(i)    
    check.append(cnt)
if check.count(max(check)) >= 2:
    print('?')
else:
    max = check.index(max(check))
    print(word_set[max])