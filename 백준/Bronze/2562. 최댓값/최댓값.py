temp = [0,0,0,0,0,0,0,0,0]
a = 0
for i in range(0,9):
    

    temp[i] = int(input()) 

    if temp[i] > a:
        a = temp[i]
        b = i+1
print(a)
print(b)    
