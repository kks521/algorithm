from collections import deque
import sys 
maxbuffer = int(sys.stdin.readline())
buffer = deque()
while True:
    packet = int(sys.stdin.readline())
    if packet > 0 and len(buffer) < maxbuffer:
        buffer.append(packet)
    elif packet == 0 and len(buffer)>0:
        buffer.popleft()
    elif packet == -1:
        break

if buffer: 
    print(' '.join(map(str,buffer)))
else: 
    print('empty')