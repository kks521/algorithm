import sys 
chess_list = list(map(int,input().split()))
piece_num = [1,1,2,2,2,8]
index_num = 0
need = []
for i in chess_list:
    if piece_num[index_num] != i: 
        need.append(piece_num[index_num] - i)
    elif piece_num[index_num] == i: 
        need.append(piece_num[index_num] - i)
    index_num += 1 

for i in need: 
    print(i, end=' ')
