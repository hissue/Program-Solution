import sys

buffer = int(sys.stdin.readline())
box = []
packet = 0
while packet !=-1:
    packet = int(sys.stdin.readline())

    if packet == -1:
        break
    
    if packet == 0:
        box.pop(0)
    
    elif len(box) != buffer:
        box.append(packet)

if len(box) == 0:
    print('empty')
else:
    print(*box)