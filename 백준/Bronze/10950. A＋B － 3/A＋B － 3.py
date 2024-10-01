a = int(input())
save = []

for i in range(0,a):    
    x, y = map(int,input().split())
    save.append(x+y)

for i in range(0,a):
    print(save[i])