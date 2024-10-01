def vps(a):
    stack = []
    for char in a:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack: 
                return 'NO'
            stack.pop()
    return 'YES' if not stack else 'NO'

     
N = int(input())
VPS = []

for i in range(N):  
    a = input()
    VPS.append(vps(a))

for i in range(N):
    print(VPS[i])