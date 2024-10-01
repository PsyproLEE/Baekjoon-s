def push(i):
    global queue, Back
    queue.append(i)
    Back += 1

def pop():
    global queue, Front, Back
    if Front == Back:
        return -1
    else:
        tmp = queue[Front]
        Front += 1
        return tmp

def size():
    return Back - Front

def empty():
    if Front == Back:
        return 1
    else:
        return 0

def front():
    if Front < Back:
        return queue[Front]
    else:
        return -1

def back():
    if Front < Back:
        return queue[Back - 1]
    else:
        return -1

Front = Back = 0
queue = []
Result = []

N = int(input())
for _ in range(N):
    a = input().split()
    
    if a[0] == 'push':
        push(a[1])
    
    if a[0] == 'pop':
        Result.append(pop())
    
    if a[0] == 'size':
        Result.append(size())
    
    if a[0] == 'empty':
        Result.append(empty())
    
    if a[0] == 'front':
        Result.append(front())
    
    if a[0] == 'back':
        Result.append(back())

for i in Result:
    print(i)