import sys

def push(data):
    arr.append(data)
            
def pop():
    pop_object = None
    if len(arr) == 0:
        pop_object = -1
    else:
        pop_object = arr.pop(0)
                
    return pop_object
    
def front():
    top_object = None
    if len(arr) == 0:
        front_object = -1
    else:
        front_object = arr[0]
                
    return front_object
                
def back():
    top_object = None
    if len(arr) == 0:
        back_object = -1
    else:
        back_object = arr[-1]
                
    return back_object
                
                
def empty():
    is_empty = False
    if len(arr) == 0:
        is_empty = 1
    else:
        is_empty = 0
    return is_empty
        
def size():
    return len(arr)

N = int(sys.stdin.readline())
arr = []
results = [sys.stdin.readline().split() for i in range(N)]
for result in results:
    if result[0] == 'push':
        push(int(result[1]))
    elif result[0] == 'pop':
        print(pop())
    elif result[0] == 'size':
        print(size())
    elif result[0] == 'empty':
        print(empty())
    elif result[0] == 'front':
        print(front())
    else:
        print(back())