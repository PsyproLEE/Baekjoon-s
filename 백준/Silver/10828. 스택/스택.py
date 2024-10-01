def top():
    global TOP, stack
    if (TOP > -1):
        return stack[len(stack)-1]
    else:
        return -1
    
def empty():
    global TOP, stack
    if (TOP == -1):
        return 1
    else:
        return 0
    
def push(i):
    global TOP, stack
    stack.append(i)
    TOP += 1
    

def pop():
    global TOP, stack
    if (TOP == -1):
        return -1
    else:
        TOP -= 1
        return stack.pop()
def size():
    return len(stack)


TOP= -1
stack = []
Result =[]


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
    
    if a[0] == 'top':
        Result.append(top())

for i in range(len(Result)):
    print(Result[i])