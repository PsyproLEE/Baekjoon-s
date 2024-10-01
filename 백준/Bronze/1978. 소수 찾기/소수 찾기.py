N = int(input())
a = list(map(int,input().split()))
save = []

for i in range(N):     
    is_prime = True
    if a[i] < 2:  
        continue
    for j in range(2,int(a[i])):
        if a[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        save.append(a[i])

print(len(save))