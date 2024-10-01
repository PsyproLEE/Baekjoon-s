N, M = map(int, input().split())
Card = list(map(int, input().split()))


Card.sort(reverse=True)
sum_max = 0


for i in range(N):
    for j in range(i + 1, N): #삼중포문
        for k in range(j + 1, N):  #i+1, j+1
            temp = Card[i] + Card[j] + Card[k]  
            if temp <= M and temp > sum_max:  
                sum_max = temp  

print(sum_max)  
